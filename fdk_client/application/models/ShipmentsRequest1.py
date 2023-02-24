"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .DataUpdates import DataUpdates

from .Products1 import Products1

from .ReasonsData1 import ReasonsData1




class ShipmentsRequest1(BaseSchema):
    # Order swagger.json

    
    data_updates = fields.Nested(DataUpdates, required=False)
    
    products = fields.List(fields.Nested(Products1, required=False), required=False)
    
    reasons = fields.Nested(ReasonsData1, required=False)
    
    identifier = fields.Str(required=False)
    

