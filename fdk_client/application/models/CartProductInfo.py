"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductPriceInfo import ProductPriceInfo

from .CartProductIdentifer import CartProductIdentifer

from .CartProduct import CartProduct



from .PromoMeta import PromoMeta



from .ProductPriceInfo import ProductPriceInfo

from .AppliedPromotion import AppliedPromotion





from .ProductAvailability import ProductAvailability

from .ProductArticle import ProductArticle








class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    discount = fields.Str(required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    promotion_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    coupon_message = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    quantity = fields.Int(required=False)
    
    key = fields.Str(required=False)
    
    message = fields.Str(required=False)
    

