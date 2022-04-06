"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .AppliedPromotion import AppliedPromotion







from .ProductAvailability import ProductAvailability



from .ProductPriceInfo import ProductPriceInfo



from .ProductPriceInfo import ProductPriceInfo

from .PromoMeta import PromoMeta



from .ProductArticle import ProductArticle

from .CartProduct import CartProduct

from .CartProductIdentifer import CartProductIdentifer


class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    discount = fields.Str(required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    promotion_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    key = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    is_set = fields.Boolean(required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    message = fields.Str(required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    coupon_message = fields.Str(required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    

