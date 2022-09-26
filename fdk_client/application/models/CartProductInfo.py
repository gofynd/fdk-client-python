"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductPriceInfo import ProductPriceInfo

from .PromoMeta import PromoMeta









from .ProductPriceInfo import ProductPriceInfo

from .AppliedPromotion import AppliedPromotion

from .ProductAvailability import ProductAvailability



from .CartProduct import CartProduct

from .CartProductIdentifer import CartProductIdentifer





from .ProductArticle import ProductArticle


class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    is_set = fields.Boolean(required=False)
    
    key = fields.Str(required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    discount = fields.Str(required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    coupon_message = fields.Str(required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    message = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    

