#!/usr/bin/env python3
"""
render_report.py

Render a SignalScan report from structured JSON data using a Jinja2 template.  Supports
both HTML and Markdown templates.  The input JSON should follow the structure
defined in `reports/report-data.example.json`.  The template may reference
keys in the JSON and use Jinja2 control structures.

Usage:
    python render_report.py --input data.json --template template.html --output report.html
"""

import argparse
import json
import os

from jinja2 import Environment, FileSystemLoader, select_autoescape


def load_data(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def render(data, template_path):
    # Determine template directory and file name
    template_dir = os.path.dirname(template_path) or '.'
    template_file = os.path.basename(template_path)
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template(template_file)
    return template.render(**data)


def main():
    parser = argparse.ArgumentParser(description='Render a SignalScan report from JSON')
    parser.add_argument('--input', required=True, help='Path to the JSON input data')
    parser.add_argument('--template', required=True, help='Path to the Jinja2 template file')
    parser.add_argument('--output', required=True, help='Path to save the rendered report')
    args = parser.parse_args()
    data = load_data(args.input)
    rendered = render(data, args.template)
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(rendered)
    print(f"Report rendered to {args.output}")


if __name__ == '__main__':
    main()