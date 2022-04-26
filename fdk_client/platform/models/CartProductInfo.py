"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductAvailability import ProductAvailability





from .ProductPriceInfo import ProductPriceInfo

from .CartProduct import CartProduct









from .AppliedPromotion import AppliedPromotion

from .ProductPriceInfo import ProductPriceInfo





from .PromoMeta import PromoMeta

from .ProductArticle import ProductArticle

from .CartProductIdentifer import CartProductIdentifer


class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    availability = fields.Nested(ProductAvailability, required=False)
    
    is_set = fields.Boolean(required=False)
    
    key = fields.Str(required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    coupon_message = fields.Str(required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    discount = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    message = fields.Str(required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    

