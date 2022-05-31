"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .CartProduct import CartProduct







from .PromoMeta import PromoMeta

from .ProductPriceInfo import ProductPriceInfo

from .ProductPriceInfo import ProductPriceInfo



from .AppliedPromotion import AppliedPromotion

from .ProductArticle import ProductArticle

from .ProductAvailability import ProductAvailability





from .CartProductIdentifer import CartProductIdentifer


class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    is_set = fields.Boolean(required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    message = fields.Str(required=False)
    
    coupon_message = fields.Str(required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    discount = fields.Str(required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    quantity = fields.Int(required=False)
    
    key = fields.Str(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    

