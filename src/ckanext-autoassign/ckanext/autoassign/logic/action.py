import ckan.plugins.toolkit as tk
import ckanext.autoassign.logic.schema as schema


@tk.side_effect_free
def autoassign_get_sum(context, data_dict):
    tk.check_access(
        "autoassign_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.autoassign_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'autoassign_get_sum': autoassign_get_sum,
    }
