"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class GTIN(BaseSchema):
    #  swagger.json

    
    gtin_type = fields.Str(required=False)
    
    gtin_value = fields.Raw(required=False)
    
    primary = fields.Boolean(required=False)
    
