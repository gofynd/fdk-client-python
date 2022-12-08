"""poscart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .SharedCart import SharedCart





class SharedCartResponse(BaseSchema):
    #  swagger.json

    
    cart = fields.Nested(SharedCart, required=False)
    
    error = fields.Str(required=False)
    
