#lib
from cerberus import Validator

class Schemas:

    def validate_pet_schema(self, response_text: dict) -> bool: 
        category_schema = self._custom_dict_schema(
            id='integer',
            name='string'
        )
        tags_schema = self._custom_dict_list_schema(
            id='integer',
            name='string'
        )

        schema_pet = {
            'id': {'type': 'integer'},
            'category':category_schema,
            'name': {'type': 'string'},
            'photoUrls': {'type': 'list','schema':{ 'type': 'string'}},
            'tags': tags_schema,
            'status': {'type': 'string'}
        }

        return self._validate_schema(schema_model=schema_pet, schema_to_validate=response_text)

    def validate_user_schema(self, response_dict: dict) -> bool:
        schema_user = {
            'code':{'type':'integer'},
            'type':{'type':'string'},
            'message':{'type':'string'}
        }

        return self._validate_schema(schema_model=schema_user, schema_to_validate=response_dict)

    @staticmethod
    def _validate_schema(schema_model: dict, schema_to_validate: dict) -> bool:
        validator = Validator(schema_model, require_all=True)
        return validator.validate(schema_to_validate)

    @staticmethod 
    def _custom_dict_list_schema(**custom_attributes) -> dict:
        item_schema = {}

        for key, value in custom_attributes.items():
            item_schema[key] = {'type': value}
        
        dict_list_schema = {
            'type': 'list', 'schema': {
                'type': 'dict', 'schema': item_schema
            }
        }

        return dict_list_schema

    @staticmethod
    def _custom_dict_schema(**custom_atributes) -> dict:
        item_schema = {}
        
        for key, value in custom_atributes.items():
            item_schema[key] = {'type': value}
        
        dict_schema = {
            'type': 'dict', 'schema': item_schema
        }

        return dict_schema