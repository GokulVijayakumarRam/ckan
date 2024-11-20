import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import logging

class CustomValidationPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IValidators)

    # IConfigurer
    def update_config(self, config_):
        # Add resources, templates, and assets if necessary
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("assets", "custom_validation")

        # Add the validator to `user_create_validators` setting
        current_validators = config_.get('ckan.auth.user_create_validators', '')
        config_['ckan.auth.user_create_validators'] = current_validators + ' email_domain_validator'
        logging.warning("email_domain_validator added to user_create_validators.")

    # IValidators
    def get_validators(self):
        # Register the validator in CKAN
        return {
            'email_domain_validator': self.email_domain_validator
        }

    def email_domain_validator(self, key, data, errors, context):
        # This validator will be called when a user registers
        email = data.get(key)
        logging.warning("Validator called for email: %s", email)
        if email and email.endswith('@rothamsted.ac.uk'):
            errors[key].append("Registration with email addresses ending in '@rothamsted.ac.uk' is not allowed.")
