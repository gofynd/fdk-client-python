"""Cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .AddProductCart import AddProductCart



class AddCartRequest(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(AddProductCart, required=False), required=False)
    
