"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










from .ProductArticle import ProductArticle



from .CartProduct import CartProduct



from .ProductPriceInfo import ProductPriceInfo









from .PromoMeta import PromoMeta





from .AppliedPromotion import AppliedPromotion



from .ProductAvailability import ProductAvailability



from .ProductPriceInfo import ProductPriceInfo





from .CartProductIdentifer import CartProductIdentifer



class CartProductInfo(BaseSchema):
    #  swagger.json

    
    bulk_offer = fields.Dict(required=False)
    
    quantity = fields.Int(required=False)
    
    discount = fields.Str(required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    message = fields.Str(required=False)
    
    coupon_message = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    is_set = fields.Boolean(required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
