"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductPriceInfo import ProductPriceInfo

from .ProductPriceInfo import ProductPriceInfo









from .AppliedPromotion import AppliedPromotion



from .CartProduct import CartProduct



from .PromoMeta import PromoMeta

from .ProductArticle import ProductArticle



from .ProductAvailability import ProductAvailability



from .CartProductIdentifer import CartProductIdentifer


class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    coupon_message = fields.Str(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    key = fields.Str(required=False)
    
    discount = fields.Str(required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    message = fields.Str(required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    quantity = fields.Int(required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    is_set = fields.Boolean(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    

