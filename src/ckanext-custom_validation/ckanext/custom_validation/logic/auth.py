import ckan.plugins.toolkit as tk


@tk.auth_allow_anonymous_access
def custom_validation_get_sum(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "custom_validation_get_sum": custom_validation_get_sum,
    }
