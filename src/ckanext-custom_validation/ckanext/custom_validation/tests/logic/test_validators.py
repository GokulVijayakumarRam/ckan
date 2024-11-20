"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.custom_validation.logic import validators


def test_custom_validation_reauired_with_valid_value():
    assert validators.custom_validation_required("value") == "value"


def test_custom_validation_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.custom_validation_required(None)
