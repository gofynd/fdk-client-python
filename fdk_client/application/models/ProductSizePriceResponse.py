"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductStockPrice import ProductStockPrice







from .MarketPlaceSttributes import MarketPlaceSttributes







from .ProductStockPrice import ProductStockPrice



from .ReturnConfig import ReturnConfig

from .Seller import Seller

from .StrategyWiseListing import StrategyWiseListing



from .ProductSet import ProductSet

from .Store import Store

from .ArticleAssignment import ArticleAssignment




class ProductSizePriceResponse(BaseSchema):
    # Catalog swagger.json

    
    price_per_piece = fields.Nested(ProductStockPrice, required=False)
    
    seller_count = fields.Int(required=False)
    
    discount = fields.Str(required=False)
    
    item_type = fields.Str(required=False)
    
    marketplace_attributes = fields.List(fields.Nested(MarketPlaceSttributes, required=False), required=False)
    
    article_id = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    special_badge = fields.Str(required=False)
    
    price = fields.Nested(ProductStockPrice, required=False)
    
    quantity = fields.Int(required=False)
    
    return_config = fields.Nested(ReturnConfig, required=False)
    
    seller = fields.Nested(Seller, required=False)
    
    strategy_wise_listing = fields.List(fields.Nested(StrategyWiseListing, required=False), required=False)
    
    trader = fields.List(fields.Str(required=False), required=False)
    
    set = fields.Nested(ProductSet, required=False)
    
    store = fields.Nested(Store, required=False)
    
    article_assignment = fields.Nested(ArticleAssignment, required=False)
    
    long_lat = fields.List(fields.Float(required=False), required=False)
    

