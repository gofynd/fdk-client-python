"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .JsonSchema import JsonSchema





class InventoryValidator(BaseSchema):
    #  swagger.json

    
    json_schema = fields.List(fields.Nested(JsonSchema, required=False), required=False)
    
    browser_script = fields.Str(required=False)
    
