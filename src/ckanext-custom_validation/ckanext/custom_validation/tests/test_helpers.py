"""Tests for helpers.py."""

import ckanext.custom_validation.helpers as helpers


def test_custom_validation_hello():
    assert helpers.custom_validation_hello() == "Hello, custom_validation!"
