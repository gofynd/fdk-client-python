"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Page import Page

from .Filters import Filters

from .OrderItems import OrderItems


class OrderList(BaseSchema):
    # Order swagger.json

    
    page = fields.Nested(Page, required=False)
    
    filters = fields.Nested(Filters, required=False)
    
    items = fields.List(fields.Nested(OrderItems, required=False), required=False)
    

