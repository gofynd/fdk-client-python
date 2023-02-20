"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CartProductIdentifer import CartProductIdentifer



from .ProductPriceInfo import ProductPriceInfo







from .ProductPriceInfo import ProductPriceInfo



from .PromoMeta import PromoMeta



from .ProductArticle import ProductArticle



from .ProductAvailability import ProductAvailability













from .AppliedPromotion import AppliedPromotion



from .CartProduct import CartProduct





class CartProductInfo(BaseSchema):
    #  swagger.json

    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    message = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    is_set = fields.Boolean(required=False)
    
    coupon_message = fields.Str(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    quantity = fields.Int(required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    discount = fields.Str(required=False)
    
