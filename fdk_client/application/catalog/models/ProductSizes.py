"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ProductSizeStores import ProductSizeStores



from .SizeChart import SizeChart



from .ProductSize import ProductSize





from .ProductListingPrice import ProductListingPrice





class ProductSizes(BaseSchema):
    #  swagger.json

    
    stores = fields.Nested(ProductSizeStores, required=False)
    
    size_chart = fields.Nested(SizeChart, required=False)
    
    sizes = fields.List(fields.Nested(ProductSize, required=False), required=False)
    
    sellable = fields.Boolean(required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    discount = fields.Str(required=False)
    
