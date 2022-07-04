"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductPriceInfo import ProductPriceInfo

from .ProductPriceInfo import ProductPriceInfo





from .PromoMeta import PromoMeta







from .CartProductIdentifer import CartProductIdentifer

from .ProductAvailability import ProductAvailability

from .ProductArticle import ProductArticle





from .AppliedPromotion import AppliedPromotion



from .CartProduct import CartProduct


class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    coupon_message = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    quantity = fields.Int(required=False)
    
    message = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    discount = fields.Str(required=False)
    
    product = fields.Nested(CartProduct, required=False)
    

