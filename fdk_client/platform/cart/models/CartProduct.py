"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ProductImage import ProductImage



from .CategoryInfo import CategoryInfo





from .ProductAction import ProductAction









from .NetQuantity import NetQuantity



from .BaseInfo import BaseInfo



class CartProduct(BaseSchema):
    #  swagger.json

    
    images = fields.List(fields.Nested(ProductImage, required=False), required=False)
    
    categories = fields.List(fields.Nested(CategoryInfo, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    action = fields.Nested(ProductAction, required=False)
    
    type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    brand = fields.Nested(BaseInfo, required=False)
    
