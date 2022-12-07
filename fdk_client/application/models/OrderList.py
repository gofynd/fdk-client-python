"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .OrderSchema import OrderSchema

from .OrderFilters import OrderFilters

from .OrderPage import OrderPage


class OrderList(BaseSchema):
    # Order swagger.json

    
    items = fields.List(fields.Nested(OrderSchema, required=False), required=False)
    
    filters = fields.Nested(OrderFilters, required=False)
    
    page = fields.Nested(OrderPage, required=False)
    

