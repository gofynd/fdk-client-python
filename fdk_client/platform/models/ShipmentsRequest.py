"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .DataUpdates import DataUpdates

from .ReasonsData import ReasonsData



from .Products import Products


class ShipmentsRequest(BaseSchema):
    # Order swagger.json

    
    data_updates = fields.Nested(DataUpdates, required=False)
    
    reasons = fields.Nested(ReasonsData, required=False)
    
    identifier = fields.Str(required=False)
    
    products = fields.List(fields.Nested(Products, required=False), required=False)
    

