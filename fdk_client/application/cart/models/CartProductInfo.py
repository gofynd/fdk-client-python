"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ProductPriceInfo import ProductPriceInfo



from .ProductArticle import ProductArticle



from .AppliedPromotion import AppliedPromotion



from .ProductPriceInfo import ProductPriceInfo



from .CartProductIdentifer import CartProductIdentifer









from .ProductAvailability import ProductAvailability









from .CartProduct import CartProduct







from .PromoMeta import PromoMeta



class CartProductInfo(BaseSchema):
    #  swagger.json

    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    is_set = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    discount = fields.Str(required=False)
    
    coupon_message = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    key = fields.Str(required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
