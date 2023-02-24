"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ProductsDataUpdatesFilters1 import ProductsDataUpdatesFilters1


class ProductsDataUpdates1(BaseSchema):
    # Order swagger.json

    
    data = fields.Dict(required=False)
    
    filters = fields.List(fields.Nested(ProductsDataUpdatesFilters1, required=False), required=False)
    

