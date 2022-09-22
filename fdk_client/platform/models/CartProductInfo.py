"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PromoMeta import PromoMeta

from .CartProductIdentifer import CartProductIdentifer





from .ProductAvailability import ProductAvailability

from .ProductPriceInfo import ProductPriceInfo

from .AppliedPromotion import AppliedPromotion



from .ProductArticle import ProductArticle

from .CartProduct import CartProduct

from .ProductPriceInfo import ProductPriceInfo










class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    message = fields.Str(required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    is_set = fields.Boolean(required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    discount = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    coupon_message = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    

