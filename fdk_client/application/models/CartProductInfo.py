"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CartProductIdentifer import CartProductIdentifer



from .ProductPriceInfo import ProductPriceInfo

from .PromoMeta import PromoMeta



from .ProductAvailability import ProductAvailability







from .AppliedPromotion import AppliedPromotion

from .ProductArticle import ProductArticle

from .ProductPriceInfo import ProductPriceInfo







from .CartProduct import CartProduct


class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    quantity = fields.Int(required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    is_set = fields.Boolean(required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    message = fields.Str(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    discount = fields.Str(required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    coupon_message = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    product = fields.Nested(CartProduct, required=False)
    

