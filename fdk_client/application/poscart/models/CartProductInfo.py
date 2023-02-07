"""poscart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .CartProductIdentifer import CartProductIdentifer





from .PromoMeta import PromoMeta



from .ProductArticle import ProductArticle





from .ProductAvailability import ProductAvailability



from .ProductPriceInfo import ProductPriceInfo









from .CartProduct import CartProduct





from .AppliedPromotion import AppliedPromotion



from .ProductPriceInfo import ProductPriceInfo







class CartProductInfo(BaseSchema):
    #  swagger.json

    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    message = fields.Str(required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    discount = fields.Str(required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    coupon_message = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    is_set = fields.Boolean(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
