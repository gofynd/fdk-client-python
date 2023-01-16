"""poscart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .ProductPriceInfo import ProductPriceInfo



from .ProductAvailability import ProductAvailability











from .CartProductIdentifer import CartProductIdentifer



from .ProductPriceInfo import ProductPriceInfo







from .CartProduct import CartProduct



from .AppliedPromotion import AppliedPromotion



from .PromoMeta import PromoMeta



from .ProductArticle import ProductArticle



class CartProductInfo(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    quantity = fields.Int(required=False)
    
    key = fields.Str(required=False)
    
    discount = fields.Str(required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    is_set = fields.Boolean(required=False)
    
    coupon_message = fields.Str(required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
