"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ProductSizePriceResponseV3 import ProductSizePriceResponseV3



from .Page import Page



from .ProductSizeSellerFilterSchemaV2 import ProductSizeSellerFilterSchemaV2



class ProductSizeSellersResponseV3(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(ProductSizePriceResponseV3, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    sort_on = fields.List(fields.Nested(ProductSizeSellerFilterSchemaV2, required=False), required=False)
    
