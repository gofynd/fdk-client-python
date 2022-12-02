"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Products import Products



from .DataUpdates import DataUpdates


class ShipmentsRequest(BaseSchema):
    # Order swagger.json

    
    products = fields.List(fields.Nested(Products, required=False), required=False)
    
    reasons = fields.List(fields.Dict(required=False), required=False)
    
    data_updates = fields.Nested(DataUpdates, required=False)
    

