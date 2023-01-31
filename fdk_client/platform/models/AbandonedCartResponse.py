"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .AbandonedCart import AbandonedCart





from .Page import Page


class AbandonedCartResponse(BaseSchema):
    # Cart swagger.json

    
    success = fields.Boolean(required=False)
    
    items = fields.List(fields.Nested(AbandonedCart, required=False), required=False)
    
    result = fields.Dict(required=False)
    
    message = fields.Str(required=False)
    
    page = fields.Nested(Page, required=False)
    

