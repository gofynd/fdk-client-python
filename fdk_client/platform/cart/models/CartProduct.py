"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CategoryInfo import CategoryInfo





from .ProductImage import ProductImage



from .ProductAction import ProductAction



from .BaseInfo import BaseInfo







from .NetQuantity import NetQuantity





class CartProduct(BaseSchema):
    #  swagger.json

    
    categories = fields.List(fields.Nested(CategoryInfo, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    images = fields.List(fields.Nested(ProductImage, required=False), required=False)
    
    action = fields.Nested(ProductAction, required=False)
    
    brand = fields.Nested(BaseInfo, required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    type = fields.Str(required=False)
    