"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .CartProductIdentifer import CartProductIdentifer

from .ProductArticle import ProductArticle





from .AppliedPromotion import AppliedPromotion



from .ProductPriceInfo import ProductPriceInfo

from .CartProduct import CartProduct

from .ProductPriceInfo import ProductPriceInfo

from .PromoMeta import PromoMeta

from .ProductAvailability import ProductAvailability




class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    key = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    discount = fields.Str(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    message = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    promotion_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    coupon_message = fields.Str(required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    bulk_offer = fields.Dict(required=False)
    

