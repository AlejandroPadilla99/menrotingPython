import json
from cerberus import Validator

class Schemas():
    
    def __init__(self):
        self.schema_pet = {
            'id': {'type': 'integer'},
            'category': {},
            'name': {'type': 'string'},
            'photoUrl': {'type': 'array', 'items': {'type': 'string'}},
            'tags': {'type': 'array', 
                'Tag': {
                    'id': {'type': 'integer'},
                    'name': {'type': 'string'}
                }
            },
            'status': {'type': 'string'}
        } 

    def validate_pet_schema(self, response_text):
        validator = Validator(self.schema_pet, require_all=True)
        response_schema_json = json.loads(response_text)
        return validator.validate(response_schema_json)
