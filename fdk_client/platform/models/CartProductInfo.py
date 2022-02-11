"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .PromoMeta import PromoMeta



from .CartProduct import CartProduct

from .ProductPriceInfo import ProductPriceInfo





from .CartProductIdentifer import CartProductIdentifer

from .ProductAvailability import ProductAvailability



from .AppliedPromotion import AppliedPromotion

from .ProductPriceInfo import ProductPriceInfo



from .ProductArticle import ProductArticle




class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    bulk_offer = fields.Dict(required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    message = fields.Str(required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    is_set = fields.Boolean(required=False)
    
    coupon_message = fields.Str(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    key = fields.Str(required=False)
    
    promotion_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    quantity = fields.Int(required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    discount = fields.Str(required=False)
    

