"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Products import Products




class ShipmentsRequest(BaseSchema):
    # OrderManage swagger.json

    
    products = fields.List(fields.Nested(Products, required=False), required=False)
    
    reasons = fields.List(fields.Dict(required=False), required=False)
    

