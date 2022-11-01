"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class ListingPriceFeature(BaseSchema):
    #  swagger.json

    
    value = fields.Str(required=False)
    
    sort = fields.Str(required=False)
    
