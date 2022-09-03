"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ProductPriceInfo import ProductPriceInfo



from .ProductAvailability import ProductAvailability





from .ProductPriceInfo import ProductPriceInfo

from .ProductArticle import ProductArticle



from .CartProduct import CartProduct





from .CartProductIdentifer import CartProductIdentifer

from .AppliedPromotion import AppliedPromotion

from .PromoMeta import PromoMeta


class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    is_set = fields.Boolean(required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    key = fields.Str(required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    quantity = fields.Int(required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    discount = fields.Str(required=False)
    
    coupon_message = fields.Str(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    

