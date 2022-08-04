"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductArticle import ProductArticle

from .ProductPriceInfo import ProductPriceInfo





from .ProductPriceInfo import ProductPriceInfo

from .AppliedPromotion import AppliedPromotion

from .ProductAvailability import ProductAvailability









from .CartProduct import CartProduct



from .PromoMeta import PromoMeta



from .CartProductIdentifer import CartProductIdentifer


class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    article = fields.Nested(ProductArticle, required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    discount = fields.Str(required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    coupon_message = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    key = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    is_set = fields.Boolean(required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    

