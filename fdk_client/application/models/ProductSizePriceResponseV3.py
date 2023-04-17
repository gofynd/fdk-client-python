"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ArticleAssignmentV3 import ArticleAssignmentV3

from .ProductSetV3 import ProductSetV3

from .SellerV3 import SellerV3







from .ProductStockPriceV3 import ProductStockPriceV3





from .ProductStockUnitPriceV3 import ProductStockUnitPriceV3



from .SellerGroupAttributes import SellerGroupAttributes

from .ProductStockPriceV3 import ProductStockPriceV3

from .MarketPlaceSttributesSchemaV3 import MarketPlaceSttributesSchemaV3



from .StrategyWiseListingSchemaV3 import StrategyWiseListingSchemaV3



from .StoreV3 import StoreV3



from .ReturnConfigSchemaV3 import ReturnConfigSchemaV3


class ProductSizePriceResponseV3(BaseSchema):
    # Catalog swagger.json

    
    article_id = fields.Str(required=False)
    
    article_assignment = fields.Nested(ArticleAssignmentV3, required=False)
    
    set = fields.Nested(ProductSetV3, required=False)
    
    seller = fields.Nested(SellerV3, required=False)
    
    seller_count = fields.Int(required=False)
    
    pincode = fields.Int(required=False)
    
    is_gift = fields.Boolean(required=False)
    
    price_per_piece = fields.Nested(ProductStockPriceV3, required=False)
    
    discount = fields.Str(required=False)
    
    is_cod = fields.Boolean(required=False)
    
    price_per_unit = fields.Nested(ProductStockUnitPriceV3, required=False)
    
    quantity = fields.Int(required=False)
    
    grouped_attributes = fields.List(fields.Nested(SellerGroupAttributes, required=False), required=False)
    
    price = fields.Nested(ProductStockPriceV3, required=False)
    
    marketplace_attributes = fields.List(fields.Nested(MarketPlaceSttributesSchemaV3, required=False), required=False)
    
    special_badge = fields.Str(required=False)
    
    strategy_wise_listing = fields.List(fields.Nested(StrategyWiseListingSchemaV3, required=False), required=False)
    
    long_lat = fields.List(fields.Float(required=False), required=False)
    
    store = fields.Nested(StoreV3, required=False)
    
    item_type = fields.Str(required=False)
    
    return_config = fields.Nested(ReturnConfigSchemaV3, required=False)
    

