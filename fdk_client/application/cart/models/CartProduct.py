"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ProductImage import ProductImage





from .NetQuantity import NetQuantity





from .BaseInfo import BaseInfo



from .ProductAction import ProductAction





from .CategoryInfo import CategoryInfo





class CartProduct(BaseSchema):
    #  swagger.json

    
    images = fields.List(fields.Nested(ProductImage, required=False), required=False)
    
    name = fields.Str(required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    type = fields.Str(required=False)
    
    brand = fields.Nested(BaseInfo, required=False)
    
    action = fields.Nested(ProductAction, required=False)
    
    slug = fields.Str(required=False)
    
    categories = fields.List(fields.Nested(CategoryInfo, required=False), required=False)
    
    uid = fields.Int(required=False)
    
