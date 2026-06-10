# Tools

This folder contains Python scripts that support the SignalScan service.  They are designed to be safe by default, respect scope and avoid intrusive behaviour.

## signalscan_collect.py

Passive collector for SignalScan.  Reads a YAML configuration file and performs a series of non‑intrusive checks on the primary domain and approved related domains:

- DNS records (A, AAAA, MX, TXT, NS) and detection of SPF and DMARC.
- TLS certificate subject, issuer and validity dates.
- HTTP response details with redirect chains and response time.
- Basic HTML insights such as page title, meta description, form count, contact links, policy links and third‑party script domains.

### Usage

```bash
python tools/signalscan_collect.py --config path/to/config.yaml
```

Include `--dry-run` to list domains without performing requests.  The script writes a JSON file to the `output_directory` specified in the YAML config.

See `config.example.yaml` for the configuration structure.

## render_report.py

Renders a SignalScan report from structured JSON data using a Jinja2 template.  Supports both HTML and Markdown templates.

### Usage

```bash
python tools/render_report.py --input path/to/data.json --template reports/signalscan-report-template.html --output path/to/report.html
```

Adjust the template parameter to use the Markdown template if desired.

## validate_engagement.py

Validates a YAML engagement configuration file to ensure required fields are present and that domains and competitor lists meet basic criteria.  Use this before running the collector to catch common errors.

### Usage

```bash
python tools/validate_engagement.py --config path/to/config.yaml
```

Returns a non‑zero exit code if the configuration is invalid.

## Tests

Unit tests are provided in the `tests/` subfolder and can be run with `pytest`:

```bash
pytest tools/tests
```

These tests verify configuration validation, a simple priority scoring function and basic report rendering.

## Dependencies

See `requirements.txt` for a list of Python dependencies.  Install them in a virtual environment before running the tools:

```bash
python -m venv venv
source venv/bin/activate
pip install -r tools/requirements.txt
```