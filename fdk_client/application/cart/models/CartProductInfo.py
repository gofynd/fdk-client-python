"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .ProductPriceInfo import ProductPriceInfo



from .PromoMeta import PromoMeta





from .ProductArticle import ProductArticle





from .CartProductIdentifer import CartProductIdentifer







from .ProductPriceInfo import ProductPriceInfo



from .AppliedPromotion import AppliedPromotion





from .CartProduct import CartProduct





from .ProductAvailability import ProductAvailability





class CartProductInfo(BaseSchema):
    #  swagger.json

    
    discount = fields.Str(required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    quantity = fields.Int(required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    is_set = fields.Boolean(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    key = fields.Str(required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    message = fields.Str(required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    coupon_message = fields.Str(required=False)
    
