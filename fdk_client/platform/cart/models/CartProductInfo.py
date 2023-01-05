"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .AppliedPromotion import AppliedPromotion



from .ProductAvailability import ProductAvailability



from .ProductPriceInfo import ProductPriceInfo



from .ProductPriceInfo import ProductPriceInfo







from .PromoMeta import PromoMeta







from .CartProductIdentifer import CartProductIdentifer



from .CartProduct import CartProduct



from .ProductArticle import ProductArticle









class CartProductInfo(BaseSchema):
    #  swagger.json

    
    discount = fields.Str(required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    is_set = fields.Boolean(required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    coupon_message = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    message = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    bulk_offer = fields.Dict(required=False)
    
