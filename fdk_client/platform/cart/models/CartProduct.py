"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .ProductAction import ProductAction



from .CategoryInfo import CategoryInfo





from .ProductImage import ProductImage





from .NetQuantity import NetQuantity



from .BaseInfo import BaseInfo





class CartProduct(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    action = fields.Nested(ProductAction, required=False)
    
    categories = fields.List(fields.Nested(CategoryInfo, required=False), required=False)
    
    slug = fields.Str(required=False)
    
    images = fields.List(fields.Nested(ProductImage, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    brand = fields.Nested(BaseInfo, required=False)
    
    type = fields.Str(required=False)
    
