"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class Weight(BaseSchema):
    #  swagger.json

    
    unit = fields.Str(required=False)
    
    shipping = fields.Int(required=False)
    
    is_default = fields.Boolean(required=False)
    
