"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class ReturnConfigResponse(BaseSchema):
    #  swagger.json

    
    unit = fields.Str(required=False)
    
    returnable = fields.Boolean(required=False)
    
    time = fields.Int(required=False)
    
