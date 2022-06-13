"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CartProduct import CartProduct



from .ProductAvailability import ProductAvailability

from .ProductPriceInfo import ProductPriceInfo







from .CartProductIdentifer import CartProductIdentifer

from .ProductPriceInfo import ProductPriceInfo

from .PromoMeta import PromoMeta



from .AppliedPromotion import AppliedPromotion



from .ProductArticle import ProductArticle




class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    product = fields.Nested(CartProduct, required=False)
    
    quantity = fields.Int(required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    discount = fields.Str(required=False)
    
    coupon_message = fields.Str(required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    is_set = fields.Boolean(required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    message = fields.Str(required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    key = fields.Str(required=False)
    

