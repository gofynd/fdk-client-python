"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .AppliedPromotion import AppliedPromotion

from .PromoMeta import PromoMeta

from .ProductAvailability import ProductAvailability



from .ProductPriceInfo import ProductPriceInfo



from .CartProduct import CartProduct





from .ProductArticle import ProductArticle







from .ProductPriceInfo import ProductPriceInfo

from .CartProductIdentifer import CartProductIdentifer




class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    is_set = fields.Boolean(required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    message = fields.Str(required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    quantity = fields.Int(required=False)
    
    coupon_message = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    discount = fields.Str(required=False)
    

