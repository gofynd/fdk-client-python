"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ProductSortOn import ProductSortOn



from .ProductFilters import ProductFilters





class GetCollectionQueryOptionResponse(BaseSchema):
    #  swagger.json

    
    sort_on = fields.List(fields.Nested(ProductSortOn, required=False), required=False)
    
    filters = fields.List(fields.Nested(ProductFilters, required=False), required=False)
    
    operators = fields.Dict(required=False)
    
