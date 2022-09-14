"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductPriceInfo import ProductPriceInfo

from .AppliedPromotion import AppliedPromotion







from .PromoMeta import PromoMeta



from .ProductPriceInfo import ProductPriceInfo





from .ProductArticle import ProductArticle

from .ProductAvailability import ProductAvailability

from .CartProductIdentifer import CartProductIdentifer

from .CartProduct import CartProduct




class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    discount = fields.Str(required=False)
    
    coupon_message = fields.Str(required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    message = fields.Str(required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    is_set = fields.Boolean(required=False)
    
    quantity = fields.Int(required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    key = fields.Str(required=False)
    

