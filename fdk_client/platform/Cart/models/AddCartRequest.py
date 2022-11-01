"""Cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .AddProductCart import AddProductCart



class AddCartRequest(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(AddProductCart, required=False), required=False)
    
