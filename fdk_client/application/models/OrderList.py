"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Filters import Filters

from .Page import Page

from .OrderItems import OrderItems


class OrderList(BaseSchema):
    # Order swagger.json

    
    filters = fields.Nested(Filters, required=False)
    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(OrderItems, required=False), required=False)
    

