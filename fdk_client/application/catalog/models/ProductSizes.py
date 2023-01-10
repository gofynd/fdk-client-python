"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .SizeChart import SizeChart





from .ProductListingPrice import ProductListingPrice







from .ProductSize import ProductSize



from .ProductSizeStores import ProductSizeStores



class ProductSizes(BaseSchema):
    #  swagger.json

    
    size_chart = fields.Nested(SizeChart, required=False)
    
    sellable = fields.Boolean(required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    multi_size = fields.Boolean(required=False)
    
    discount = fields.Str(required=False)
    
    sizes = fields.List(fields.Nested(ProductSize, required=False), required=False)
    
    stores = fields.Nested(ProductSizeStores, required=False)
    
