"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .ProductsDataUpdatesFilters import ProductsDataUpdatesFilters



class ProductsDataUpdates(BaseSchema):
    #  swagger.json

    
    data = fields.Dict(required=False)
    
    filters = fields.List(fields.Nested(ProductsDataUpdatesFilters, required=False), required=False)
    
