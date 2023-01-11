"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .ProductImage import ProductImage



from .NetQuantity import NetQuantity





from .CategoryInfo import CategoryInfo





from .BaseInfo import BaseInfo





from .ProductAction import ProductAction



class CartProduct(BaseSchema):
    #  swagger.json

    
    type = fields.Str(required=False)
    
    images = fields.List(fields.Nested(ProductImage, required=False), required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    slug = fields.Str(required=False)
    
    categories = fields.List(fields.Nested(CategoryInfo, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    brand = fields.Nested(BaseInfo, required=False)
    
    name = fields.Str(required=False)
    
    action = fields.Nested(ProductAction, required=False)
    
