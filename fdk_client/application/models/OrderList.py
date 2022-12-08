"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .OrderFilters import OrderFilters

from .OrderSchema import OrderSchema

from .OrderPage import OrderPage


class OrderList(BaseSchema):
    # Order swagger.json

    
    filters = fields.Nested(OrderFilters, required=False)
    
    items = fields.List(fields.Nested(OrderSchema, required=False), required=False)
    
    page = fields.Nested(OrderPage, required=False)
    

