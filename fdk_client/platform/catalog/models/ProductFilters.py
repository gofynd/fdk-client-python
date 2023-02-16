"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ProductFiltersValue import ProductFiltersValue



from .ProductFiltersKey import ProductFiltersKey



class ProductFilters(BaseSchema):
    #  swagger.json

    
    values = fields.List(fields.Nested(ProductFiltersValue, required=False), required=False)
    
    key = fields.Nested(ProductFiltersKey, required=False)
    
