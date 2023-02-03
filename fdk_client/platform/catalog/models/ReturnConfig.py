"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class ReturnConfig(BaseSchema):
    #  swagger.json

    
    time = fields.Int(required=False)
    
    returnable = fields.Boolean(required=False)
    
    unit = fields.Str(required=False)
    
