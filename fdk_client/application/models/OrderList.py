"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .OrderFilters import OrderFilters

from .OrderPage import OrderPage

from .OrderSchema import OrderSchema


class OrderList(BaseSchema):
    # Order swagger.json

    
    filters = fields.Nested(OrderFilters, required=False)
    
    page = fields.Nested(OrderPage, required=False)
    
    items = fields.List(fields.Nested(OrderSchema, required=False), required=False)
    

