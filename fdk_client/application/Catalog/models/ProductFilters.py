"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ProductFiltersKey import ProductFiltersKey



from .ProductFiltersValue import ProductFiltersValue



class ProductFilters(BaseSchema):
    #  swagger.json

    
    key = fields.Nested(ProductFiltersKey, required=False)
    
    values = fields.List(fields.Nested(ProductFiltersValue, required=False), required=False)
    
