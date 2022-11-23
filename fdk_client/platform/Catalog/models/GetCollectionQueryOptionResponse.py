"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .ProductFilters import ProductFilters



from .ProductSortOn import ProductSortOn



class GetCollectionQueryOptionResponse(BaseSchema):
    #  swagger.json

    
    operators = fields.Dict(required=False)
    
    filters = fields.List(fields.Nested(ProductFilters, required=False), required=False)
    
    sort_on = fields.List(fields.Nested(ProductSortOn, required=False), required=False)
    
