"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .ProductsDataUpdatesFilters1 import ProductsDataUpdatesFilters1



class ProductsDataUpdates1(BaseSchema):
    #  swagger.json

    
    data = fields.Dict(required=False)
    
    filters = fields.List(fields.Nested(ProductsDataUpdatesFilters1, required=False), required=False)
    
