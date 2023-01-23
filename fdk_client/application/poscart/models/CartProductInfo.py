"""poscart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .PromoMeta import PromoMeta



from .ProductPriceInfo import ProductPriceInfo





from .ProductArticle import ProductArticle







from .ProductPriceInfo import ProductPriceInfo











from .AppliedPromotion import AppliedPromotion



from .ProductAvailability import ProductAvailability



from .CartProduct import CartProduct



from .CartProductIdentifer import CartProductIdentifer



class CartProductInfo(BaseSchema):
    #  swagger.json

    
    is_set = fields.Boolean(required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    quantity = fields.Int(required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    coupon_message = fields.Str(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    discount = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
