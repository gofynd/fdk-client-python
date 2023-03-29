"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Products1 import Products1

from .ReasonsData1 import ReasonsData1



from .DataUpdates import DataUpdates


class ShipmentsRequest1(BaseSchema):
    # Order swagger.json

    
    products = fields.List(fields.Nested(Products1, required=False), required=False)
    
    reasons = fields.Nested(ReasonsData1, required=False)
    
    identifier = fields.Str(required=False)
    
    data_updates = fields.Nested(DataUpdates, required=False)
    

