import json
from unicodedata import category
from cerberus import Validator

class Schemas():
    
    def __init__(self):
        category_schema = {
            'id': {'type': 'integer'},
            'name': {'type': 'string'},
        }

        tags_schema = {
            'id': {'type': 'integer'},
            'name': {'type': 'string'},
        }

        self.schema_pet = {
            'id': {'type': 'integer'},
            'category': {'type': 'list',
               'schema': category_schema
            },
            'name': {'type': 'string'},
            'tags': {'type': 'list',
                'schema': tags_schema
            },
            'status': {'type': 'string'}
        }

    def validate_pet_schema(self, response_text):
        validator = Validator(self.schema_pet, require_all=True)
        response_schema_json = json.loads(response_text)
        return validator.validate(response_schema_json)
