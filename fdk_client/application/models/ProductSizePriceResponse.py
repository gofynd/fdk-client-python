"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ArticleAssignment import ArticleAssignment





from .Seller import Seller

from .ProductStockPrice import ProductStockPrice

from .StrategyWiseListing import StrategyWiseListing

from .MarketPlaceSttributes import MarketPlaceSttributes



from .ReturnConfig import ReturnConfig









from .Store import Store



from .ProductSet import ProductSet

from .ProductStockPrice import ProductStockPrice


class ProductSizePriceResponse(BaseSchema):
    # Catalog swagger.json

    
    quantity = fields.Int(required=False)
    
    article_assignment = fields.Nested(ArticleAssignment, required=False)
    
    discount = fields.Str(required=False)
    
    article_id = fields.Str(required=False)
    
    seller = fields.Nested(Seller, required=False)
    
    price_per_piece = fields.Nested(ProductStockPrice, required=False)
    
    strategy_wise_listing = fields.List(fields.Nested(StrategyWiseListing, required=False), required=False)
    
    marketplace_attributes = fields.List(fields.Nested(MarketPlaceSttributes, required=False), required=False)
    
    seller_count = fields.Int(required=False)
    
    return_config = fields.Nested(ReturnConfig, required=False)
    
    special_badge = fields.Str(required=False)
    
    trader = fields.List(fields.Str(required=False), required=False)
    
    item_type = fields.Str(required=False)
    
    long_lat = fields.List(fields.Float(required=False), required=False)
    
    store = fields.Nested(Store, required=False)
    
    pincode = fields.Int(required=False)
    
    set = fields.Nested(ProductSet, required=False)
    
    price = fields.Nested(ProductStockPrice, required=False)
    

