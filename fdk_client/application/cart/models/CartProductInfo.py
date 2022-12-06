"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .CartProduct import CartProduct



from .ProductPriceInfo import ProductPriceInfo



from .ProductPriceInfo import ProductPriceInfo



from .ProductAvailability import ProductAvailability





from .CartProductIdentifer import CartProductIdentifer





from .AppliedPromotion import AppliedPromotion



from .PromoMeta import PromoMeta













from .ProductArticle import ProductArticle



class CartProductInfo(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    discount = fields.Str(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    key = fields.Str(required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    quantity = fields.Int(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    is_set = fields.Boolean(required=False)
    
    coupon_message = fields.Str(required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
