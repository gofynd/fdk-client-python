"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ProductBrand import ProductBrand



from .ProductBrand import ProductBrand



from .ProductBrand import ProductBrand



class ProductCategoryMap(BaseSchema):
    #  swagger.json

    
    l1 = fields.Nested(ProductBrand, required=False)
    
    l2 = fields.Nested(ProductBrand, required=False)
    
    l3 = fields.Nested(ProductBrand, required=False)
    
