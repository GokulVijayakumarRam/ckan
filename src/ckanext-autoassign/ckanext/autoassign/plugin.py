import ckan.plugins as p
import ckan.plugins.toolkit as tk
import ckan.model as model

class AutoassignPlugin(p.SingletonPlugin):
    p.implements(p.IConfigurer)
    p.implements(p.IActions)

    def update_config(self, config):
        tk.add_template_directory(config, 'templates')

    def get_actions(self):
        return {
            'user_create': self.custom_user_create
        }

    def custom_user_create(self, context, data_dict):
        # Call the original 'user_create' action
        user = tk.get_action('user_create')(context, data_dict)
        email = user.get('email')
        organization_name = "Rothamsted"

        if email and email.endswith('@rothamsted.ac.uk'):
            organization = model.Group.get(organization_name)
            if organization:
                user_obj = model.User.get(user['id'])
                model.Session.add(user_obj)
                model.Session.commit()
                context['model'] = model
                context['user'] = tk.c.user
                # tk.get_action('organization_member_create')(context, {
                #     'id': organization.id,
                #     'username': user_obj.name,
                #     'role': 'editor'
                # })

        return user
