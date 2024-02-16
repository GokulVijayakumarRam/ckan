# encoding: utf-8
from __future__ import annotations

from ckan.types import Schema
import ckan.plugins as p
from ckan.plugins.toolkit import Invalid
import ckan.plugins.toolkit as tk

class ExampleIDatasetFormPlugin(tk.DefaultDatasetForm, p.SingletonPlugin):
    p.implements(p.IDatasetForm)
    p.implements(p.IConfigurer)

    def create_package_schema(self) -> Schema:
        # let's grab the default schema in our plugin
        schema: Schema = super(
            ExampleIDatasetFormPlugin, self).create_package_schema()
        # our custom field
        schema.update({

            'given_name': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'family_name': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'creator': [tk.get_validator('not_empty'),
                            tk.get_converter('convert_to_extras')],
            'nameIdentifier': [tk.get_validator('not_empty'),
                            tk.get_converter('convert_to_extras')],
            'creatorAffiliation': [tk.get_validator('not_empty'),
                            tk.get_converter('convert_to_extras')],
            'publisher': [tk.get_validator('not_empty'),
                            tk.get_converter('convert_to_extras')],    
            'publicationYear': [tk.get_validator('not_empty'), tk.get_validator('year_validator'),
                                 tk.get_converter('convert_to_extras')], 
            'abstract': [tk.get_validator('not_empty'),
                                 tk.get_converter('convert_to_extras')],
            'methods': [tk.get_validator('not_empty'),
                                 tk.get_converter('convert_to_extras')],
            'technicalInfo': [tk.get_validator('ignore_missing'),
                                 tk.get_converter('convert_to_extras')],
            'experimentCode': [tk.get_validator('not_empty'),
                            tk.get_converter('convert_to_extras')],
            'Codes': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],            
            'resourceTypeGeneral': [tk.get_validator('not_empty'),
                                 tk.get_converter('convert_to_extras')],
            'resourceType': [tk.get_validator('not_empty'),
                                 tk.get_converter('convert_to_extras')],
            'language': [tk.get_validator('ignore_missing'),
                                 tk.get_converter('convert_to_extras')],
            'funderName': [tk.get_validator('not_empty'),
                                 tk.get_converter('convert_to_extras')],
            'funderIdentifier': [tk.get_validator('not_empty'),
                                 tk.get_converter('convert_to_extras')],
            'contributorDetails': [tk.get_validator('ignore_missing'),
                                 tk.get_converter('convert_to_extras')],
            'contributorId': [tk.get_validator('ignore_missing'),
                                 tk.get_converter('convert_to_extras')],
            'contributorType': [tk.get_validator('ignore_missing'),
                                 tk.get_converter('convert_to_extras')],
            'contributorAffiliation': [tk.get_validator('ignore_missing'),
                                 tk.get_converter('convert_to_extras')]
                      
        })        
        return schema
    def update_package_schema(self) -> Schema:
        schema: Schema = super(
            ExampleIDatasetFormPlugin, self).update_package_schema()
        # our custom field
        schema.update({

            'given_name': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'family_name': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'creator': [tk.get_validator('not_empty'),
                            tk.get_converter('convert_to_extras')],
            'nameIdentifier': [tk.get_validator('not_empty'),
                            tk.get_converter('convert_to_extras')],
            'creatorAffiliation': [tk.get_validator('not_empty'),
                            tk.get_converter('convert_to_extras')],
            'publisher': [tk.get_validator('not_empty'),
                            tk.get_converter('convert_to_extras')],                            
            'publicationYear': [tk.get_validator('not_empty'), tk.get_validator('year_validator'),
                                 tk.get_converter('convert_to_extras')], 
            'abstract': [tk.get_validator('not_empty'),
                                 tk.get_converter('convert_to_extras')],
            'methods': [tk.get_validator('not_empty'),
                                 tk.get_converter('convert_to_extras')],
            'technicalInfo': [tk.get_validator('ignore_missing'),
                                 tk.get_converter('convert_to_extras')],
            'experimentCode': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'Codes': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'resourceTypeGeneral': [tk.get_validator('not_empty'),
                                 tk.get_converter('convert_to_extras')],
            'resourceType': [tk.get_validator('not_empty'),
                                 tk.get_converter('convert_to_extras')],
            'language': [tk.get_validator('ignore_missing'),
                                 tk.get_converter('convert_to_extras')],
            'funderName': [tk.get_validator('not_empty'),
                                 tk.get_converter('convert_to_extras')],   
            'funderIdentifier': [tk.get_validator('not_empty'),
                                 tk.get_converter('convert_to_extras')],   
            'contributorDetails': [tk.get_validator('ignore_missing'),
                                 tk.get_converter('convert_to_extras')],   
            'contributorId': [tk.get_validator('ignore_missing'),
                                 tk.get_converter('convert_to_extras')],   
            'contributorType': [tk.get_validator('ignore_missing'),
                                 tk.get_converter('convert_to_extras')],   
            'contributorAffiliation': [tk.get_validator('ignore_missing'),
                                 tk.get_converter('convert_to_extras')]                           
        })       
        return schema
    def show_package_schema(self) -> Schema:
        schema: Schema = super(
            ExampleIDatasetFormPlugin, self).show_package_schema()
        schema.update({

            'given_name': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'family_name': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'creator': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'nameIdentifier': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'creatorAffiliation': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'publisher': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'publicationYear': [tk.get_converter('convert_from_extras'),
                                 tk.get_validator('ignore_missing')],
            'abstract': [tk.get_converter('convert_from_extras'),
                                 tk.get_validator('ignore_missing')],
            'methods': [tk.get_converter('convert_from_extras'),
                                 tk.get_validator('ignore_missing')],
            'technicalInfo': [tk.get_converter('convert_from_extras'),
                                 tk.get_validator('ignore_missing')],
            'experimentCode': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'Codes': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'resourceTypeGeneral': [tk.get_converter('convert_from_extras'),
                                 tk.get_validator('ignore_missing')],
            'resourceType': [tk.get_converter('convert_from_extras'),
                                 tk.get_validator('ignore_missing')],
            'language': [tk.get_converter('convert_from_extras'),
                                 tk.get_validator('ignore_missing')],
            'funderName': [tk.get_converter('convert_from_extras'),
                                 tk.get_validator('ignore_missing')],
            'funderIdentifier': [tk.get_converter('convert_from_extras'),
                                 tk.get_validator('ignore_missing')],
            'contributorDetails': [tk.get_converter('convert_from_extras'),
                                 tk.get_validator('ignore_missing')],
            'contributorId': [tk.get_converter('convert_from_extras'),
                                 tk.get_validator('ignore_missing')],
            'contributorType': [tk.get_converter('convert_from_extras'),
                                 tk.get_validator('ignore_missing')],
            'contributorAffiliation': [tk.get_converter('convert_from_extras'),
                                 tk.get_validator('ignore_missing')]
        })       
        return schema

        schema: Schema = super(
            ExampleIDatasetFormPlugin, self).show_package_schema()
        schema.update({

            'given_name': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'family_name': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'creator': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'nameIdentifier': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'creatorAffiliation': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'publisher': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'publicationYear': [tk.get_converter('convert_from_extras'),
                                 tk.get_validator('ignore_missing')],
            'abstract': [tk.get_converter('convert_from_extras'),
                                 tk.get_validator('ignore_missing')],
            'methods': [tk.get_converter('convert_from_extras'),
                                 tk.get_validator('ignore_missing')],
            'technicalInfo': [tk.get_converter('convert_from_extras'),
                                 tk.get_validator('ignore_missing')],
            'experimentCode': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'Codes': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'resourceTypeGeneral': [tk.get_converter('convert_from_extras'),
                                 tk.get_validator('ignore_missing')],
            'resourceType': [tk.get_converter('convert_from_extras'),
                                 tk.get_validator('ignore_missing')],
            'language': [tk.get_converter('convert_from_extras'),
                                 tk.get_validator('ignore_missing')],
            'funderName': [tk.get_converter('convert_from_extras'),
                                 tk.get_validator('ignore_missing')],
            'funderIdentifier': [tk.get_converter('convert_from_extras'),
                                 tk.get_validator('ignore_missing')],
            'contributorDetails': [tk.get_converter('convert_from_extras'),
                                 tk.get_validator('ignore_missing')],
            'contributorId': [tk.get_converter('convert_from_extras'),
                                 tk.get_validator('ignore_missing')],
            'contributorType': [tk.get_converter('convert_from_extras'),
                                 tk.get_validator('ignore_missing')],
            'contributorAffiliation': [tk.get_converter('convert_from_extras'),
                                 tk.get_validator('ignore_missing')]                        
        })       
        return schema

    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self) -> list[str]:
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []
    def update_config(self, config: CKANConfig):
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        tk.add_template_directory(config, 'templates')        
