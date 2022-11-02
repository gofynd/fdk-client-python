"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .OrderItems import OrderItems

from .Page import Page

from .Filters import Filters


class OrderList(BaseSchema):
    # Order swagger.json

    
    items = fields.List(fields.Nested(OrderItems, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    filters = fields.Nested(Filters, required=False)
    

