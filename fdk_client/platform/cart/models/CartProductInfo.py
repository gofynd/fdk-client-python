"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














from .CartProduct import CartProduct



from .ProductAvailability import ProductAvailability



from .PromoMeta import PromoMeta



from .CartProductIdentifer import CartProductIdentifer







from .ProductPriceInfo import ProductPriceInfo



from .ProductPriceInfo import ProductPriceInfo



from .ProductArticle import ProductArticle



from .AppliedPromotion import AppliedPromotion





class CartProductInfo(BaseSchema):
    #  swagger.json

    
    key = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    coupon_message = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    discount = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    bulk_offer = fields.Dict(required=False)
    