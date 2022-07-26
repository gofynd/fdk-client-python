"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ProductArticle import ProductArticle

from .PromoMeta import PromoMeta

from .CartProductIdentifer import CartProductIdentifer



from .ProductPriceInfo import ProductPriceInfo

from .ProductAvailability import ProductAvailability



from .AppliedPromotion import AppliedPromotion



from .ProductPriceInfo import ProductPriceInfo







from .CartProduct import CartProduct


class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    is_set = fields.Boolean(required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    message = fields.Str(required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    discount = fields.Str(required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    quantity = fields.Int(required=False)
    
    key = fields.Str(required=False)
    
    coupon_message = fields.Str(required=False)
    
    product = fields.Nested(CartProduct, required=False)
    

