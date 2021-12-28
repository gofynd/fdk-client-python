"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema



from .ReturnConfig import ReturnConfig

from .Seller import Seller





from .ProductStockPrice import ProductStockPrice

from .StrategyWiseListing import StrategyWiseListing

from .Store import Store

from .ArticleAssignment import ArticleAssignment

from .ProductStockPrice import ProductStockPrice









from .ProductSet import ProductSet



from .MarketPlaceSttributes import MarketPlaceSttributes


class ProductSizePriceResponse(BaseSchema):
    # Catalog swagger.json

    
    seller_count = fields.Int(required=False)
    
    return_config = fields.Nested(ReturnConfig, required=False)
    
    seller = fields.Nested(Seller, required=False)
    
    quantity = fields.Int(required=False)
    
    discount = fields.Str(required=False)
    
    price = fields.Nested(ProductStockPrice, required=False)
    
    strategy_wise_listing = fields.List(fields.Nested(StrategyWiseListing, required=False), required=False)
    
    store = fields.Nested(Store, required=False)
    
    article_assignment = fields.Nested(ArticleAssignment, required=False)
    
    price_per_piece = fields.Nested(ProductStockPrice, required=False)
    
    article_id = fields.Str(required=False)
    
    item_type = fields.Str(required=False)
    
    long_lat = fields.List(fields.Float(required=False), required=False)
    
    special_badge = fields.Str(required=False)
    
    set = fields.Nested(ProductSet, required=False)
    
    pincode = fields.Int(required=False)
    
    marketplace_attributes = fields.List(fields.Nested(MarketPlaceSttributes, required=False), required=False)
    

