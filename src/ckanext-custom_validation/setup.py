# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    # If you are changing from the default layout of your extension, you may
    # have to change the message extractors, you can read more about babel
    # message extraction at
    # http://babel.pocoo.org/docs/messages/#extraction-method-mapping-and-configuration
    packages=find_packages(),
    entry_points='''
        [ckan.plugins]
        custom_validation=ckanext.custom_validation.plugin:CustomValidationPlugin
    ''',
    message_extractors={
        'ckanext': [
            ('**.py', 'python', None),
            ('**.js', 'javascript', None),
            ('**/templates/**.html', 'ckan', None),
        ],
    },
    install_requires=[]
)
