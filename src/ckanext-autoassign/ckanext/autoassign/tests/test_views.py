"""Tests for views.py."""

import pytest

import ckanext.autoassign.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "autoassign")
@pytest.mark.usefixtures("with_plugins")
def test_autoassign_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("autoassign.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, autoassign!"
