"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductPriceInfo import ProductPriceInfo

from .ProductPriceInfo import ProductPriceInfo



from .CartProductIdentifer import CartProductIdentifer



from .ProductArticle import ProductArticle



from .PromoMeta import PromoMeta

from .AppliedPromotion import AppliedPromotion





from .ProductAvailability import ProductAvailability



from .CartProduct import CartProduct




class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    discount = fields.Str(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    message = fields.Str(required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    quantity = fields.Int(required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    promotion_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    is_set = fields.Boolean(required=False)
    
    coupon_message = fields.Str(required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    key = fields.Str(required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    bulk_offer = fields.Dict(required=False)
    

