"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .ProductAvailability import ProductAvailability







from .CartProductIdentifer import CartProductIdentifer



from .ProductArticle import ProductArticle

from .AppliedPromotion import AppliedPromotion

from .CartProduct import CartProduct

from .ProductPriceInfo import ProductPriceInfo





from .ProductPriceInfo import ProductPriceInfo

from .PromoMeta import PromoMeta


class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    coupon_message = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    message = fields.Str(required=False)
    
    discount = fields.Str(required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    is_set = fields.Boolean(required=False)
    
    quantity = fields.Int(required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    

