"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .AppliedPromotion import AppliedPromotion

from .ProductArticle import ProductArticle





from .ProductPriceInfo import ProductPriceInfo

from .ProductAvailability import ProductAvailability



from .PromoMeta import PromoMeta

from .ProductPriceInfo import ProductPriceInfo

from .CartProduct import CartProduct

from .CartProductIdentifer import CartProductIdentifer






class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    discount = fields.Str(required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    is_set = fields.Boolean(required=False)
    
    key = fields.Str(required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    quantity = fields.Int(required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    message = fields.Str(required=False)
    
    coupon_message = fields.Str(required=False)
    

