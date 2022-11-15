"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .Page import Page



from .ProductSizePriceResponseV2 import ProductSizePriceResponseV2



from .ProductSizeSellerFilterSchemaV2 import ProductSizeSellerFilterSchemaV2



class ProductSizeSellersResponseV2(BaseSchema):
    #  swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(ProductSizePriceResponseV2, required=False), required=False)
    
    sort_on = fields.List(fields.Nested(ProductSizeSellerFilterSchemaV2, required=False), required=False)
    
