"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ProductsReasonsData import ProductsReasonsData



from .ProductsReasonsFilters import ProductsReasonsFilters



class ProductsReasons(BaseSchema):
    #  swagger.json

    
    data = fields.Nested(ProductsReasonsData, required=False)
    
    filters = fields.List(fields.Nested(ProductsReasonsFilters, required=False), required=False)
    
