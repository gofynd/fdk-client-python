"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .AppliedPromotion import AppliedPromotion

from .CartProductIdentifer import CartProductIdentifer



from .ProductArticle import ProductArticle

from .CartProduct import CartProduct





from .PromoMeta import PromoMeta



from .CouponDetails import CouponDetails



from .ProductAvailability import ProductAvailability





from .ProductPriceInfo import ProductPriceInfo

from .ProductPriceInfo import ProductPriceInfo




class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    coupon_message = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    message = fields.Str(required=False)
    
    coupon = fields.Nested(CouponDetails, required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    discount = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    quantity = fields.Int(required=False)
    

