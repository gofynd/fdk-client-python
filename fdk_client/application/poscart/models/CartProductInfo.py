"""poscart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .CartProduct import CartProduct





from .ProductPriceInfo import ProductPriceInfo



from .ProductAvailability import ProductAvailability



from .CartProductIdentifer import CartProductIdentifer











from .ProductArticle import ProductArticle





from .ProductPriceInfo import ProductPriceInfo



from .PromoMeta import PromoMeta



from .AppliedPromotion import AppliedPromotion



class CartProductInfo(BaseSchema):
    #  swagger.json

    
    discount = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    key = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    message = fields.Str(required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    coupon_message = fields.Str(required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
