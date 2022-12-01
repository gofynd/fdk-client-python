"""theme Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class GlobalSchemaProps(BaseSchema):
    #  swagger.json

    
    id = fields.Str(required=False)
    
    label = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    category = fields.Str(required=False)
    
