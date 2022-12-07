"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class GTIN(BaseSchema):
    #  swagger.json

    
    primary = fields.Boolean(required=False)
    
    gtin_type = fields.Str(required=False)
    
    gtin_value = fields.Str(required=False)
    
