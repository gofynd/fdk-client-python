"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class ApplicationItemMOQ(BaseSchema):
    #  swagger.json

    
    maximum = fields.Int(required=False)
    
    minimum = fields.Int(required=False)
    
    increment_unit = fields.Int(required=False)
    
