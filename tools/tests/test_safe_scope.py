import tempfile
import yaml
import pytest

from tools.validate_engagement import validate


def test_valid_config():
    config = {
        'client_name': 'Test',
        'primary_domain': 'example.invalid',
        'approved_related_domains': ['blog.example.invalid'],
        'public_profile_urls': [],
        'competitor_urls': ['a.com', 'b.com', 'c.com'],
        'output_directory': './out'
    }
    # Should not raise
    validate(config)


def test_invalid_primary_in_approved():
    config = {
        'client_name': 'Test',
        'primary_domain': 'example.invalid',
        'approved_related_domains': ['example.invalid'],
        'public_profile_urls': [],
        'competitor_urls': ['a.com', 'b.com', 'c.com'],
        'output_directory': './out'
    }
    with pytest.raises(ValueError):
        validate(config)


def test_competitor_count():
    config = {
        'client_name': 'Test',
        'primary_domain': 'example.invalid',
        'approved_related_domains': [],
        'public_profile_urls': [],
        'competitor_urls': ['a.com', 'b.com'],
        'output_directory': './out'
    }
    with pytest.raises(ValueError):
        validate(config)