"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class MOQ(BaseSchema):
    #  swagger.json

    
    minimum = fields.Int(required=False)
    
    increment_unit = fields.Int(required=False)
    
    maximum = fields.Int(required=False)
    
