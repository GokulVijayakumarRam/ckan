import ckan.plugins.toolkit as tk


def custom_validation_required(value):
    if not value or value is tk.missing:
        raise tk.Invalid(tk._("Required"))
    return value


def get_validators():
    return {
        "custom_validation_required": custom_validation_required,
    }
