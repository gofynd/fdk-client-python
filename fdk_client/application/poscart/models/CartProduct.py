"""poscart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .CategoryInfo import CategoryInfo



from .ProductImage import ProductImage





from .NetQuantity import NetQuantity



from .ProductAction import ProductAction



from .BaseInfo import BaseInfo







class CartProduct(BaseSchema):
    #  swagger.json

    
    uid = fields.Int(required=False)
    
    categories = fields.List(fields.Nested(CategoryInfo, required=False), required=False)
    
    images = fields.List(fields.Nested(ProductImage, required=False), required=False)
    
    slug = fields.Str(required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    action = fields.Nested(ProductAction, required=False)
    
    brand = fields.Nested(BaseInfo, required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
