"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .OrderDataSet import OrderDataSet




class OrderListingResponse(BaseSchema):
    # Orders swagger.json

    
    orders = fields.List(fields.Nested(OrderDataSet, required=False), required=False)
    
    success = fields.Boolean(required=False)
    

