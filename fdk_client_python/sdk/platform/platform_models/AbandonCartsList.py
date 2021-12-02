"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .AbandonCartsDetail import AbandonCartsDetail



from .Page import Page


class AbandonCartsList(BaseSchema):

    
    items = fields.List(fields.Nested(AbandonCartsDetail, required=False), required=False)
    
    cart_total = fields.Str(required=False)
    
    page = fields.Nested(Page, required=False)
    

