"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class ManufacturerResponse1(BaseSchema):
    #  swagger.json

    
    address = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
