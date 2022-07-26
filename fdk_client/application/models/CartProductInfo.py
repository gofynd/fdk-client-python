"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductArticle import ProductArticle

from .CartProduct import CartProduct

from .ProductPriceInfo import ProductPriceInfo



from .CartProductIdentifer import CartProductIdentifer







from .AppliedPromotion import AppliedPromotion



from .PromoMeta import PromoMeta

from .ProductAvailability import ProductAvailability



from .ProductPriceInfo import ProductPriceInfo




class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    article = fields.Nested(ProductArticle, required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    quantity = fields.Int(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    is_set = fields.Boolean(required=False)
    
    coupon_message = fields.Str(required=False)
    
    discount = fields.Str(required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    message = fields.Str(required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    key = fields.Str(required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    bulk_offer = fields.Dict(required=False)
    

