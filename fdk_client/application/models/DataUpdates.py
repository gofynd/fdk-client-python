"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .EntitiesDataUpdates import EntitiesDataUpdates

from .ProductsDataUpdates import ProductsDataUpdates


class DataUpdates(BaseSchema):
    # Order swagger.json

    
    entities = fields.List(fields.Nested(EntitiesDataUpdates, required=False), required=False)
    
    products = fields.List(fields.Nested(ProductsDataUpdates, required=False), required=False)
    

