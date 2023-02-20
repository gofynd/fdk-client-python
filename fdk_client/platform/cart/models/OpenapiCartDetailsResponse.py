"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .CartProductInfo import CartProductInfo





from .CartBreakup import CartBreakup



class OpenapiCartDetailsResponse(BaseSchema):
    #  swagger.json

    
    is_valid = fields.Boolean(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    message = fields.Str(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
