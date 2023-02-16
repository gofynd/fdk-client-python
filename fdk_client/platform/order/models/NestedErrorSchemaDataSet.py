"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class NestedErrorSchemaDataSet(BaseSchema):
    #  swagger.json

    
    type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
