"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class ReturnConfig(BaseSchema):
    #  swagger.json

    
    returnable = fields.Boolean(required=False)
    
    unit = fields.Str(required=False)
    
    time = fields.Int(required=False)
    
