"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .StrategyWiseListingSchemaV2 import StrategyWiseListingSchemaV2



from .SellerGroupAttributes import SellerGroupAttributes



from .ProductSetV2 import ProductSetV2

from .ProductStockPriceV2 import ProductStockPriceV2

from .StoreV2 import StoreV2

from .ProductStockPriceV2 import ProductStockPriceV2

from .SellerV2 import SellerV2

from .ProductStockUnitPriceV2 import ProductStockUnitPriceV2





from .ArticleAssignmentV2 import ArticleAssignmentV2

from .ReturnConfigSchemaV2 import ReturnConfigSchemaV2

from .MarketPlaceSttributesSchemaV2 import MarketPlaceSttributesSchemaV2








class ProductSizePriceResponseV2(BaseSchema):
    # Catalog swagger.json

    
    item_type = fields.Str(required=False)
    
    special_badge = fields.Str(required=False)
    
    seller_count = fields.Int(required=False)
    
    strategy_wise_listing = fields.List(fields.Nested(StrategyWiseListingSchemaV2, required=False), required=False)
    
    quantity = fields.Int(required=False)
    
    grouped_attributes = fields.List(fields.Nested(SellerGroupAttributes, required=False), required=False)
    
    is_cod = fields.Boolean(required=False)
    
    set = fields.Nested(ProductSetV2, required=False)
    
    price = fields.Nested(ProductStockPriceV2, required=False)
    
    store = fields.Nested(StoreV2, required=False)
    
    price_per_piece = fields.Nested(ProductStockPriceV2, required=False)
    
    seller = fields.Nested(SellerV2, required=False)
    
    price_per_unit = fields.Nested(ProductStockUnitPriceV2, required=False)
    
    long_lat = fields.List(fields.Float(required=False), required=False)
    
    discount = fields.Str(required=False)
    
    article_assignment = fields.Nested(ArticleAssignmentV2, required=False)
    
    return_config = fields.Nested(ReturnConfigSchemaV2, required=False)
    
    marketplace_attributes = fields.List(fields.Nested(MarketPlaceSttributesSchemaV2, required=False), required=False)
    
    pincode = fields.Int(required=False)
    
    is_gift = fields.Boolean(required=False)
    
    article_id = fields.Str(required=False)
    

