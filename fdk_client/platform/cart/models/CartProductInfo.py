"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .ProductAvailability import ProductAvailability



from .ProductPriceInfo import ProductPriceInfo



from .AppliedPromotion import AppliedPromotion





from .CartProductIdentifer import CartProductIdentifer



from .CartProduct import CartProduct





from .ProductArticle import ProductArticle









from .ProductPriceInfo import ProductPriceInfo



from .PromoMeta import PromoMeta



class CartProductInfo(BaseSchema):
    #  swagger.json

    
    discount = fields.Str(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    key = fields.Str(required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    message = fields.Str(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    coupon_message = fields.Str(required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    is_set = fields.Boolean(required=False)
    
    quantity = fields.Int(required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
