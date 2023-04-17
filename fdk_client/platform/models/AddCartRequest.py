"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .AddProductCart import AddProductCart


class AddCartRequest(BaseSchema):
    # Cart swagger.json

    
    meta = fields.Dict(required=False)
    
    items = fields.List(fields.Nested(AddProductCart, required=False), required=False)
    

