"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ProductPriceInfo import ProductPriceInfo



from .AppliedPromotion import AppliedPromotion







from .CartProductIdentifer import CartProductIdentifer









from .PromoMeta import PromoMeta



from .ProductPriceInfo import ProductPriceInfo







from .ProductAvailability import ProductAvailability



from .ProductArticle import ProductArticle



from .CartProduct import CartProduct





class CartProductInfo(BaseSchema):
    #  swagger.json

    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    is_set = fields.Boolean(required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    key = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    discount = fields.Str(required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    coupon_message = fields.Str(required=False)
    
