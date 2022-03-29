"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Seller import Seller

from .ProductStockPrice import ProductStockPrice

from .Store1 import Store1



from .ArticleAssignment import ArticleAssignment

from .ReturnConfig import ReturnConfig



from .StrategyWiseListing import StrategyWiseListing

from .MarketPlaceSttributes import MarketPlaceSttributes







from .ProductStockPrice import ProductStockPrice







from .ProductSet import ProductSet




class ProductSizePriceResponse(BaseSchema):
    # Catalog swagger.json

    
    seller = fields.Nested(Seller, required=False)
    
    price = fields.Nested(ProductStockPrice, required=False)
    
    store = fields.Nested(Store1, required=False)
    
    trader = fields.List(fields.Dict(required=False), required=False)
    
    article_assignment = fields.Nested(ArticleAssignment, required=False)
    
    return_config = fields.Nested(ReturnConfig, required=False)
    
    seller_count = fields.Int(required=False)
    
    strategy_wise_listing = fields.List(fields.Nested(StrategyWiseListing, required=False), required=False)
    
    marketplace_attributes = fields.List(fields.Nested(MarketPlaceSttributes, required=False), required=False)
    
    pincode = fields.Int(required=False)
    
    item_type = fields.Str(required=False)
    
    special_badge = fields.Str(required=False)
    
    price_per_piece = fields.Nested(ProductStockPrice, required=False)
    
    discount = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    long_lat = fields.List(fields.Float(required=False), required=False)
    
    set = fields.Nested(ProductSet, required=False)
    
    article_id = fields.Str(required=False)
    

