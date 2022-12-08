"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CartProductIdentifer import CartProductIdentifer











from .PromoMeta import PromoMeta





from .ProductPriceInfo import ProductPriceInfo





from .ProductAvailability import ProductAvailability





from .AppliedPromotion import AppliedPromotion



from .ProductArticle import ProductArticle



from .ProductPriceInfo import ProductPriceInfo





from .CartProduct import CartProduct



class CartProductInfo(BaseSchema):
    #  swagger.json

    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    is_set = fields.Boolean(required=False)
    
    key = fields.Str(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    discount = fields.Str(required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    coupon_message = fields.Str(required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    quantity = fields.Int(required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    message = fields.Str(required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
