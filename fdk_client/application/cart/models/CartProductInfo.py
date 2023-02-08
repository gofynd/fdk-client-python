"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .CartProductIdentifer import CartProductIdentifer



from .CartProduct import CartProduct



from .ProductArticle import ProductArticle



from .PromoMeta import PromoMeta



from .ProductAvailability import ProductAvailability



from .ProductPriceInfo import ProductPriceInfo











from .ProductPriceInfo import ProductPriceInfo



from .AppliedPromotion import AppliedPromotion









class CartProductInfo(BaseSchema):
    #  swagger.json

    
    parent_item_identifiers = fields.Dict(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    is_set = fields.Boolean(required=False)
    
    coupon_message = fields.Str(required=False)
    
    discount = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    message = fields.Str(required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    key = fields.Str(required=False)
    
