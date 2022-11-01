"""Cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ProductPriceInfo import ProductPriceInfo







from .ProductAvailability import ProductAvailability







from .PromoMeta import PromoMeta





from .AppliedPromotion import AppliedPromotion



from .CartProductIdentifer import CartProductIdentifer





from .CartProduct import CartProduct



from .ProductPriceInfo import ProductPriceInfo



from .ProductArticle import ProductArticle







class CartProductInfo(BaseSchema):
    #  swagger.json

    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    key = fields.Str(required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    is_set = fields.Boolean(required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    coupon_message = fields.Str(required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    message = fields.Str(required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    quantity = fields.Int(required=False)
    
    discount = fields.Str(required=False)
    
