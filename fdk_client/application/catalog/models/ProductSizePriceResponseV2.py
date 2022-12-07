"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










from .ProductSetV2 import ProductSetV2





from .ProductStockPriceV2 import ProductStockPriceV2





from .SellerV2 import SellerV2



from .MarketPlaceSttributesSchemaV2 import MarketPlaceSttributesSchemaV2



from .ProductStockUnitPriceV2 import ProductStockUnitPriceV2





from .SellerGroupAttributes import SellerGroupAttributes





from .ArticleAssignmentV2 import ArticleAssignmentV2



from .StrategyWiseListingSchemaV2 import StrategyWiseListingSchemaV2



from .ProductStockPriceV2 import ProductStockPriceV2





from .StoreV2 import StoreV2



from .ReturnConfigSchemaV2 import ReturnConfigSchemaV2



class ProductSizePriceResponseV2(BaseSchema):
    #  swagger.json

    
    special_badge = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    seller_count = fields.Int(required=False)
    
    set = fields.Nested(ProductSetV2, required=False)
    
    discount = fields.Str(required=False)
    
    price_per_piece = fields.Nested(ProductStockPriceV2, required=False)
    
    quantity = fields.Int(required=False)
    
    seller = fields.Nested(SellerV2, required=False)
    
    marketplace_attributes = fields.List(fields.Nested(MarketPlaceSttributesSchemaV2, required=False), required=False)
    
    price_per_unit = fields.Nested(ProductStockUnitPriceV2, required=False)
    
    article_id = fields.Str(required=False)
    
    grouped_attributes = fields.List(fields.Nested(SellerGroupAttributes, required=False), required=False)
    
    long_lat = fields.List(fields.Float(required=False), required=False)
    
    article_assignment = fields.Nested(ArticleAssignmentV2, required=False)
    
    strategy_wise_listing = fields.List(fields.Nested(StrategyWiseListingSchemaV2, required=False), required=False)
    
    price = fields.Nested(ProductStockPriceV2, required=False)
    
    item_type = fields.Str(required=False)
    
    store = fields.Nested(StoreV2, required=False)
    
    return_config = fields.Nested(ReturnConfigSchemaV2, required=False)
    
