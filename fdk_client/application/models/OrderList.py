"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .OrderItems import OrderItems

from .Filters import Filters

from .Page import Page


class OrderList(BaseSchema):
    # Order swagger.json

    
    items = fields.List(fields.Nested(OrderItems, required=False), required=False)
    
    filters = fields.Nested(Filters, required=False)
    
    page = fields.Nested(Page, required=False)
    

