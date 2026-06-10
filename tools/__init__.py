"""
Core Python package for SignalScan tooling.

This ``tools`` package contains the utility scripts used for
collecting data, validating configurations and rendering reports.
Individual modules should be imported directly, for example::

    from tools.render_report import render

The presence of this ``__init__.py`` file marks this directory as a
regular Python package rather than a namespace package. The test suite
expects a top-level ``tools`` package to be importable, and since
pytest runs within the ``signalscan-launch-kit`` directory, the
relative ``tools`` folder serves that purpose.
"""

__all__ = [
    'render_report',
    'validate_engagement',
]