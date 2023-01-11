"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ProductsReasonsFilters import ProductsReasonsFilters



from .ProductsReasonsData import ProductsReasonsData



class ProductsReasons(BaseSchema):
    #  swagger.json

    
    filters = fields.List(fields.Nested(ProductsReasonsFilters, required=False), required=False)
    
    data = fields.Nested(ProductsReasonsData, required=False)
    
