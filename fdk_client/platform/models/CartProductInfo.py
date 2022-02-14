"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CartProduct import CartProduct

from .ProductPriceInfo import ProductPriceInfo

from .CartProductIdentifer import CartProductIdentifer

from .ProductAvailability import ProductAvailability





from .ProductPriceInfo import ProductPriceInfo

from .ProductArticle import ProductArticle





from .PromoMeta import PromoMeta



from .AppliedPromotion import AppliedPromotion






class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    product = fields.Nested(CartProduct, required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    message = fields.Str(required=False)
    
    discount = fields.Str(required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    quantity = fields.Int(required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    coupon_message = fields.Str(required=False)
    
    promotion_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    key = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    

