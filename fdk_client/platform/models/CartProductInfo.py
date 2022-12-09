"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .ProductAvailability import ProductAvailability

from .ProductPriceInfo import ProductPriceInfo



from .PromoMeta import PromoMeta

from .ProductArticle import ProductArticle





from .ProductPriceInfo import ProductPriceInfo





from .AppliedPromotion import AppliedPromotion



from .CartProductIdentifer import CartProductIdentifer

from .CartProduct import CartProduct


class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    is_set = fields.Boolean(required=False)
    
    key = fields.Str(required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    discount = fields.Str(required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    message = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    coupon = fields.Dict(required=False)
    
    coupon_message = fields.Str(required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    product = fields.Nested(CartProduct, required=False)
    

