from flask import Blueprint


autoassign = Blueprint(
    "autoassign", __name__)


def page():
    return "Hello, autoassign!"


autoassign.add_url_rule(
    "/autoassign/page", view_func=page)


def get_blueprints():
    return [autoassign]
