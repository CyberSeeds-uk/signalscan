# Reports

This folder contains templates, schemas and sample data for generating SignalScan reports.

## Templates

- **signalscan-report-template.html** – A comprehensive HTML report layout ready for print.  It uses Jinja2 placeholders (double curly braces and control structures) and can be rendered using `tools/render_report.py`.
- **signalscan-report-template.md** – A Markdown version of the report template using similar placeholders.  Use this if you prefer a Markdown output or need to convert to other formats.
- **three-signal-preview-template.html** – A concise one‑page preview for prospects.  It highlights one positive observation, one trust gap, one customer‑journey obstruction, one missed opportunity and includes an ethical boundary statement and call to action.

## Schemas and Data

- **finding-schema.json** – A JSON Schema defining the fields required for each finding.  Use this to validate your report data before rendering.
- **report-data.example.json** – A complete example of the data structure expected by `render_report.py`, including grouped findings, priority matrices and action lists.  It powers the sample report found in `sample-sanitised-report/`.
- **priority-matrix.csv** – An illustrative spreadsheet with formulas for calculating priority scores based on impact, urgency, ease of repair and confidence.  You can adapt the scoring system to your needs.

## Samples

The `sample-sanitised-report/` folder contains a fictional report for a made‑up company, Example Garage.  This sample includes:

- **sample-report.html** – A rendered HTML report demonstrating the final output style.
- **sample-report.md** – A Markdown version of the same report.
- **sample-findings.json** – The grouped findings used to produce the sample report.  You can use this as a starting point for your own reports.

## Rendering a Report

To generate a report from JSON data:

1. Install dependencies: `pip install -r tools/requirements.txt`.
2. Prepare a JSON file following the structure of `report-data.example.json` and validate your findings against `finding-schema.json`.
3. Run the renderer: `python tools/render_report.py --input path/to/your-data.json --template reports/signalscan-report-template.html --output path/to/report.html`.

For Markdown output, specify the Markdown template instead of the HTML template.

## Notes

Please remember that all sample data in this folder is fictional and does not represent real businesses or vulnerabilities.