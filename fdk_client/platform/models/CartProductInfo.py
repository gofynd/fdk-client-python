"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CartProduct import CartProduct

from .ProductAvailability import ProductAvailability

from .PromoMeta import PromoMeta



from .ProductPriceInfo import ProductPriceInfo



from .ProductPriceInfo import ProductPriceInfo







from .AppliedPromotion import AppliedPromotion

from .ProductArticle import ProductArticle

from .CartProductIdentifer import CartProductIdentifer






class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    product = fields.Nested(CartProduct, required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    quantity = fields.Int(required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    is_set = fields.Boolean(required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    message = fields.Str(required=False)
    
    coupon_message = fields.Str(required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    promotion_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    discount = fields.Str(required=False)
    
    key = fields.Str(required=False)
    

