"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductPriceInfo import ProductPriceInfo

from .CartProduct import CartProduct

from .ProductArticle import ProductArticle







from .ProductPriceInfo import ProductPriceInfo

from .PromoMeta import PromoMeta



from .ProductAvailability import ProductAvailability







from .AppliedPromotion import AppliedPromotion

from .CartProductIdentifer import CartProductIdentifer




class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    discount = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    key = fields.Str(required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    coupon_message = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    

