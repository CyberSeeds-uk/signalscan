import json
import os

from tools.render_report import render


def test_render_sample_report(tmp_path):
    # Load example data
    data_path = os.path.join(os.path.dirname(__file__), '..', 'report-data.example.json')
    template_path = os.path.join(os.path.dirname(__file__), '..', 'signalscan-report-template.html')
    # Adjust paths
    data_path = os.path.abspath(data_path)
    template_path = os.path.abspath(template_path)
    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    output = render(data, template_path)
    assert 'Example Garage' in output
    assert 'Privacy notice 404' in output or 'Privacy Notice 404' in output