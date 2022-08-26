"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Page import Page



from .AbandonedCart import AbandonedCart




class AbandonedCartResponse(BaseSchema):
    # Cart swagger.json

    
    page = fields.Nested(Page, required=False)
    
    message = fields.Str(required=False)
    
    result = fields.List(fields.Nested(AbandonedCart, required=False), required=False)
    
    success = fields.Boolean(required=False)
    
