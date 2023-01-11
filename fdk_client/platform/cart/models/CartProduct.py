"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .NetQuantity import NetQuantity





from .ProductAction import ProductAction







from .CategoryInfo import CategoryInfo



from .BaseInfo import BaseInfo





from .ProductImage import ProductImage



class CartProduct(BaseSchema):
    #  swagger.json

    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    uid = fields.Int(required=False)
    
    action = fields.Nested(ProductAction, required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    categories = fields.List(fields.Nested(CategoryInfo, required=False), required=False)
    
    brand = fields.Nested(BaseInfo, required=False)
    
    slug = fields.Str(required=False)
    
    images = fields.List(fields.Nested(ProductImage, required=False), required=False)
    
