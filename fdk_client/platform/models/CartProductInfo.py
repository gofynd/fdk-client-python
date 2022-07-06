"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .CartProduct import CartProduct

from .PromoMeta import PromoMeta

from .CartProductIdentifer import CartProductIdentifer





from .ProductPriceInfo import ProductPriceInfo





from .ProductAvailability import ProductAvailability

from .ProductArticle import ProductArticle



from .ProductPriceInfo import ProductPriceInfo

from .AppliedPromotion import AppliedPromotion




class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    quantity = fields.Int(required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    message = fields.Str(required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    key = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    discount = fields.Str(required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    coupon_message = fields.Str(required=False)
    

