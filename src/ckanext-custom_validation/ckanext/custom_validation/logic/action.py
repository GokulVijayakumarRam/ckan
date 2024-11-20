import ckan.plugins.toolkit as tk
import ckanext.custom_validation.logic.schema as schema


@tk.side_effect_free
def custom_validation_get_sum(context, data_dict):
    tk.check_access(
        "custom_validation_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.custom_validation_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'custom_validation_get_sum': custom_validation_get_sum,
    }
