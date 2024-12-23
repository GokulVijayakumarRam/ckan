import ckan.plugins.toolkit as tk


@tk.auth_allow_anonymous_access
def customapi_get_sum(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "customapi_get_sum": customapi_get_sum,
    }
