"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .ProductAvailability import ProductAvailability







from .ProductArticle import ProductArticle

from .ProductPriceInfo import ProductPriceInfo

from .PromoMeta import PromoMeta







from .CartProductIdentifer import CartProductIdentifer



from .ProductPriceInfo import ProductPriceInfo

from .CartProduct import CartProduct


class CartProductInfo(BaseSchema):

    
    availability = fields.Nested(ProductAvailability, required=False)
    
    key = fields.Str(required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    message = fields.Str(required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    discount = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    is_set = fields.Boolean(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    coupon_message = fields.Str(required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    product = fields.Nested(CartProduct, required=False)
    

