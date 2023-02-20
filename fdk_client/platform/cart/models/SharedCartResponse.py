"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .SharedCart import SharedCart



class SharedCartResponse(BaseSchema):
    #  swagger.json

    
    error = fields.Str(required=False)
    
    cart = fields.Nested(SharedCart, required=False)
    
