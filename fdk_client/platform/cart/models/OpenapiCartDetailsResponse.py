"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .CartBreakup import CartBreakup



from .CartProductInfo import CartProductInfo



class OpenapiCartDetailsResponse(BaseSchema):
    #  swagger.json

    
    is_valid = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
