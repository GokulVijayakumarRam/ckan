"""Tests for views.py."""

import pytest

import ckanext.custom_validation.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "custom_validation")
@pytest.mark.usefixtures("with_plugins")
def test_custom_validation_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("custom_validation.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, custom_validation!"
