#!/usr/bin/env python3
"""
signalscan_collect.py

A passive information collection tool for SignalScan.  This script reads a YAML
configuration defining the client, scope and settings, then performs a series of
non‑intrusive checks on approved domains.  Results are written to a JSON file
in the specified output directory.

Prohibited behaviour such as port scanning, brute forcing or form submission is
explicitly avoided.  The tool respects delays between requests and limits
redirect chains.

Usage:
    python signalscan_collect.py --config config.yaml [--dry-run]
"""

import argparse
import json
import os
import ssl
import socket
import time
import urllib.parse
from datetime import datetime

import yaml
import dns.resolver
import requests
from bs4 import BeautifulSoup


DEFAULT_MAX_REDIRECTS = 5


def load_config(path):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def validate_engagement(config):
    required_fields = [
        'client_name', 'primary_domain', 'approved_related_domains',
        'public_profile_urls', 'competitor_urls', 'output_directory'
    ]
    for field in required_fields:
        if field not in config:
            raise ValueError(f"Missing required field '{field}' in configuration.")
    # Basic domain validation
    primary = config['primary_domain'].strip().lower()
    if ' ' in primary or primary == '':
        raise ValueError("Primary domain is invalid.")
    # Competitor count
    if not isinstance(config['competitor_urls'], list) or len(config['competitor_urls']) != 3:
        raise ValueError("Exactly three competitor URLs must be provided.")
    # Ensure approved domains are list
    if not isinstance(config['approved_related_domains'], list):
        raise ValueError("'approved_related_domains' must be a list.")
    # Ensure no duplicates in approved domains and primary
    for d in config['approved_related_domains']:
        if d.strip().lower() == primary:
            raise ValueError("Approved related domains should not include primary domain.")


def query_dns_records(domain):
    records = {}
    resolver = dns.resolver.Resolver()
    for record_type in ['A', 'AAAA', 'MX', 'TXT', 'NS']:
        try:
            answers = resolver.resolve(domain, record_type, lifetime=5)
            records[record_type] = [r.to_text() for r in answers]
        except Exception:
            records[record_type] = []
    return records


def detect_spf(records):
    txt_records = records.get('TXT', [])
    for txt in txt_records:
        if txt.startswith('v=spf1'):
            return True
    return False


def detect_dmarc(domain):
    resolver = dns.resolver.Resolver()
    try:
        answers = resolver.resolve(f"_dmarc.{domain}", 'TXT', lifetime=5)
        return [r.to_text() for r in answers]
    except Exception:
        return []


def fetch_tls_certificate(domain):
    try:
        ctx = ssl.create_default_context()
        with socket.create_connection((domain, 443), timeout=5) as sock:
            with ctx.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                subject = dict(x[0] for x in cert.get('subject', []))
                issuer = dict(x[0] for x in cert.get('issuer', []))
                return {
                    'subject': subject,
                    'issuer': issuer,
                    'notBefore': cert.get('notBefore'),
                    'notAfter': cert.get('notAfter')
                }
    except Exception:
        return {}


def request_url(url, user_agent, delay, max_redirects=DEFAULT_MAX_REDIRECTS):
    session = requests.Session()
    session.headers.update({'User-Agent': user_agent})
    result = {
        'final_url': url,
        'status_code': None,
        'headers': {},
        'redirects': [],
        'response_time': None,
        'body': None
    }
    try:
        start = time.time()
        resp = session.get(url, allow_redirects=True, timeout=10)
        duration = time.time() - start
        result['final_url'] = resp.url
        result['status_code'] = resp.status_code
        result['headers'] = dict(resp.headers)
        result['redirects'] = [r.url for r in resp.history][:max_redirects]
        result['response_time'] = round(duration, 3)
        result['body'] = resp.text
    except Exception:
        pass
    finally:
        time.sleep(delay)
    return result


def parse_html_for_insights(html, base_url):
    soup = BeautifulSoup(html, 'html.parser') if html else None
    meta = {}
    if soup:
        # Title and description
        title_tag = soup.find('title')
        meta['title'] = title_tag.get_text().strip() if title_tag else ''
        description = ''
        desc_tag = soup.find('meta', attrs={'name': 'description'})
        if desc_tag and desc_tag.get('content'):
            description = desc_tag['content'].strip()
        meta['description'] = description
        # Forms count
        meta['form_count'] = len(soup.find_all('form'))
        # Contact links
        contacts = []
        for a in soup.find_all('a', href=True):
            href = a['href']
            if href.startswith('mailto:') or href.startswith('tel:'):
                contacts.append(href)
        meta['contact_links'] = list(set(contacts))
        # Privacy & cookie links
        priv_links = []
        for a in soup.find_all('a', href=True):
            text = (a.get_text() or '').lower()
            href = a['href']
            if any(x in text for x in ['privacy', 'cookie', 'gdpr', 'data']):
                priv_links.append(href)
        meta['policy_links'] = list(set(priv_links))
        # Third party script domains
        script_domains = []
        parsed_base = urllib.parse.urlparse(base_url).hostname or ''
        for script in soup.find_all('script', src=True):
            src = script['src']
            parsed = urllib.parse.urlparse(src)
            if parsed.hostname and parsed.hostname != parsed_base:
                script_domains.append(parsed.hostname)
        meta['third_party_scripts'] = list(set(script_domains))
    return meta


def collect_domain(domain, config):
    checks = config.get('enabled_passive_checks', [])
    delay = float(config.get('respectful_delay', 1.0))
    user_agent = config.get('user_agent', 'SignalScanBot/1.0')
    domain_data = {
        'dns_records': {},
        'spf_present': None,
        'dmarc_records': [],
        'tls_certificate': {},
        'http': {},
        'html_insights': {}
    }
    # DNS
    if 'dns_records' in checks:
        domain_data['dns_records'] = query_dns_records(domain)
        domain_data['spf_present'] = detect_spf(domain_data['dns_records'])
        domain_data['dmarc_records'] = detect_dmarc(domain)
    # TLS certificate
    if 'tls_certificate' in checks:
        domain_data['tls_certificate'] = fetch_tls_certificate(domain)
    # HTTP and HTML
    url = f'https://{domain}'
    http_info = None
    if any(c in checks for c in ['http_headers', 'robots', 'sitemap', 'homepage_metadata', 'contact_links', 'form_count', 'third_party_scripts', 'privacy_and_cookie_pages', 'mixed_content', 'response_time']):
        http_info = request_url(url, user_agent, delay)
        domain_data['http'] = {
            'final_url': http_info['final_url'],
            'status_code': http_info['status_code'],
            'headers': http_info['headers'],
            'redirects': http_info['redirects'],
            'response_time': http_info['response_time']
        }
        # parse html
        domain_data['html_insights'] = parse_html_for_insights(http_info['body'], url)
    return domain_data


def run_collection(config_path, dry_run=False):
    config = load_config(config_path)
    validate_engagement(config)
    primary_domain = config['primary_domain'].strip().lower()
    approved_domains = [d.strip().lower() for d in config.get('approved_related_domains', [])]
    timestamp = datetime.utcnow().isoformat() + 'Z'
    result = {
        'client_name': config['client_name'],
        'timestamp': timestamp,
        'domains': {},
        'public_profiles': config.get('public_profile_urls', []),
        'competitors': config.get('competitor_urls', [])
    }
    domains_to_collect = [primary_domain] + approved_domains
    if dry_run:
        print("[DRY‑RUN] Would collect data for domains:", ', '.join(domains_to_collect))
        return
    for domain in domains_to_collect:
        result['domains'][domain] = collect_domain(domain, config)
    outdir = config['output_directory']
    os.makedirs(outdir, exist_ok=True)
    outfile = os.path.join(outdir, f"{primary_domain.replace('.', '_')}_signalscan.json")
    with open(outfile, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2)
    print(f"Collection complete. Results saved to {outfile}")


def main():
    parser = argparse.ArgumentParser(description="Passive collector for SignalScan")
    parser.add_argument('--config', required=True, help='Path to YAML configuration')
    parser.add_argument('--dry-run', action='store_true', help='Perform a dry run without making requests')
    args = parser.parse_args()
    run_collection(args.config, dry_run=args.dry_run)


if __name__ == '__main__':
    main()