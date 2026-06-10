#!/usr/bin/env python3
"""
validate_engagement.py

Validate a YAML engagement configuration before running the passive collector.  The
validation ensures that required fields are present, domains are well‑formed and
the correct number of competitor URLs are supplied.  It does not perform any
network requests.

Usage:
    python validate_engagement.py --config config.yaml
"""

import argparse
import sys
import yaml


def validate(config):
    required_fields = [
        'client_name', 'primary_domain', 'approved_related_domains',
        'public_profile_urls', 'competitor_urls', 'output_directory'
    ]
    for field in required_fields:
        if field not in config:
            raise ValueError(f"Missing required field '{field}'")
    primary = config['primary_domain'].strip().lower()
    if ' ' in primary or not primary:
        raise ValueError("Primary domain is invalid")
    if not isinstance(config['competitor_urls'], list) or len(config['competitor_urls']) != 3:
        raise ValueError("Exactly three competitor URLs must be provided")
    if not isinstance(config['approved_related_domains'], list):
        raise ValueError("'approved_related_domains' must be a list")
    for d in config['approved_related_domains']:
        if d.strip().lower() == primary:
            raise ValueError("Approved related domains should not include primary domain")


def main():
    parser = argparse.ArgumentParser(description='Validate a SignalScan engagement configuration')
    parser.add_argument('--config', required=True, help='Path to YAML config file')
    args = parser.parse_args()
    with open(args.config, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    try:
        validate(config)
    except Exception as e:
        print(f"Invalid configuration: {e}", file=sys.stderr)
        sys.exit(1)
    print("Configuration is valid.")


if __name__ == '__main__':
    main()