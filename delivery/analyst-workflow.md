# Analyst Workflow

This document outlines the recommended workflow for analysts conducting a SignalScan engagement.  Follow these steps to ensure consistency and quality.

## 1. Preparation

1. Review the completed pre‑engagement checklist and ensure all required information is available.
2. Validate the YAML configuration using `tools/validate_engagement.py`.
3. Create a client folder using the naming convention `YYYYMMDD_CLIENT-SLUG_SIGNALS-SERVICE` and populate the `00-scope` folder with scope documents and signed terms.

## 2. Collection

1. Run the passive collector:
   ```bash
   python tools/signalscan_collect.py --config path/to/config.yaml
   ```
   Output files will be saved in the configured `output_directory`.  Copy or link these files into the `01-evidence` folder.
2. Manually browse the client’s website and competitors on a mobile device or emulator.  Take notes and screenshots of customer‑journey friction points and trust signals.  Save these in `01-evidence`.
3. Review public reviews and narrative elements.  Capture recurring themes and any trust gaps.  Do not copy personal information.

## 3. Analysis

1. Create individual finding records in JSON format following the schema in `reports/finding-schema.json`.  Use the naming convention `SG-[STAGE]-[NNN]`.
2. For each finding, link to supporting evidence, assign impact levels and draft interpretations and recommendations.
3. Group findings by SIGNAL stage and review for completeness.
4. Create a priority matrix (CSV or table) ranking findings by trust/security impact, commercial impact, urgency, ease of repair and confidence.

## 4. Report Assembly

1. Prepare a data file (JSON) matching the structure of `reports/report-data.example.json`.
2. Use `tools/render_report.py` to generate the HTML report:
   ```bash
   python tools/render_report.py --input your-data.json --template reports/signalscan-report-template.html --output client-report.html
   ```
3. Convert the HTML report to PDF if required using your preferred tool (e.g. browser print to PDF).  Ensure print formatting is A4 and that headings do not break across pages.
4. Save the final report and data file in the `03-report` folder.

## 5. Quality Assurance

1. Review the report using the `quality-assurance-checklist.md`.
2. Ensure all recommendations are clear, actionable and free of jargon.
3. Verify that sensitive observations are marked appropriately and that no personal data is exposed.
4. Double‑check pricing, guarantees and boundaries are consistent.

## 6. Delivery

1. Send the report to the client via secure email or shared folder.
2. Offer a walkthrough call to explain the findings and answer questions.
3. Record any immediate feedback and note any factual corrections for one revision round.

Following this workflow promotes consistency and professionalism across all engagements.