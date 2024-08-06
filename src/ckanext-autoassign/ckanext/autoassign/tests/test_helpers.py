"""Tests for helpers.py."""

import ckanext.autoassign.helpers as helpers


def test_autoassign_hello():
    assert helpers.autoassign_hello() == "Hello, autoassign!"
