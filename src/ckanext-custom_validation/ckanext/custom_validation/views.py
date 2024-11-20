from flask import Blueprint


custom_validation = Blueprint(
    "custom_validation", __name__)


def page():
    return "Hello, custom_validation!"


custom_validation.add_url_rule(
    "/custom_validation/page", view_func=page)


def get_blueprints():
    return [custom_validation]
