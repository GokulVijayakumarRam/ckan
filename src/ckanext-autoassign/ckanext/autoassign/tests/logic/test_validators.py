"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.autoassign.logic import validators


def test_autoassign_reauired_with_valid_value():
    assert validators.autoassign_required("value") == "value"


def test_autoassign_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.autoassign_required(None)
