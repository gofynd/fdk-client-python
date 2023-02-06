"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .ProductPriceInfo import ProductPriceInfo

from .CartProduct import CartProduct





from .CouponDetails import CouponDetails



from .AppliedPromotion import AppliedPromotion







from .ProductArticle import ProductArticle

from .PromoMeta import PromoMeta

from .ProductAvailability import ProductAvailability

from .CartProductIdentifer import CartProductIdentifer

from .ProductPriceInfo import ProductPriceInfo


class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    is_set = fields.Boolean(required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    quantity = fields.Int(required=False)
    
    discount = fields.Str(required=False)
    
    coupon = fields.Nested(CouponDetails, required=False)
    
    key = fields.Str(required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    coupon_message = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    

