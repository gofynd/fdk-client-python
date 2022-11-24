"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .OrderPage import OrderPage

from .OrderFilters import OrderFilters

from .OrderSchema import OrderSchema


class OrderList(BaseSchema):
    # Order swagger.json

    
    page = fields.Nested(OrderPage, required=False)
    
    filters = fields.Nested(OrderFilters, required=False)
    
    items = fields.List(fields.Nested(OrderSchema, required=False), required=False)
    

