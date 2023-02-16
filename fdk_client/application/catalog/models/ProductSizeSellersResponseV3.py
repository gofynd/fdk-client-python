"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ProductSizePriceResponseV2 import ProductSizePriceResponseV2



from .ProductSizeSellerFilterSchemaV2 import ProductSizeSellerFilterSchemaV2



from .Page import Page



class ProductSizeSellersResponseV3(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(ProductSizePriceResponseV2, required=False), required=False)
    
    sort_on = fields.List(fields.Nested(ProductSizeSellerFilterSchemaV2, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
