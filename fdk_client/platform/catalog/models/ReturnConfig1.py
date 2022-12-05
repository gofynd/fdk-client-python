"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class ReturnConfig1(BaseSchema):
    #  swagger.json

    
    unit = fields.Str(required=False)
    
    time = fields.Int(required=False)
    
    returnable = fields.Boolean(required=False)
    
