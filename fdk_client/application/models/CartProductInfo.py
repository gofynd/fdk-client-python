"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductPriceInfo import ProductPriceInfo

from .PromoMeta import PromoMeta

from .CartProductIdentifer import CartProductIdentifer









from .ProductAvailability import ProductAvailability

from .CartProduct import CartProduct







from .ProductArticle import ProductArticle

from .ProductPriceInfo import ProductPriceInfo


class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    quantity = fields.Int(required=False)
    
    key = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    coupon_message = fields.Str(required=False)
    
    discount = fields.Str(required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    

