"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .CartProduct import CartProduct





from .ProductPriceInfo import ProductPriceInfo



from .ProductPriceInfo import ProductPriceInfo













from .AppliedPromotion import AppliedPromotion







from .ProductArticle import ProductArticle



from .PromoMeta import PromoMeta



from .CartProductIdentifer import CartProductIdentifer



from .ProductAvailability import ProductAvailability



class CartProductInfo(BaseSchema):
    #  swagger.json

    
    product = fields.Nested(CartProduct, required=False)
    
    key = fields.Str(required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    coupon_message = fields.Str(required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    discount = fields.Str(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    is_set = fields.Boolean(required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    quantity = fields.Int(required=False)
    
    message = fields.Str(required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    