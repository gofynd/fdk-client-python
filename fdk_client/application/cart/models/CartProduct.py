"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .BaseInfo import BaseInfo



from .NetQuantity import NetQuantity







from .CategoryInfo import CategoryInfo



from .ProductImage import ProductImage



from .ProductAction import ProductAction





class CartProduct(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    brand = fields.Nested(BaseInfo, required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    uid = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    categories = fields.List(fields.Nested(CategoryInfo, required=False), required=False)
    
    images = fields.List(fields.Nested(ProductImage, required=False), required=False)
    
    action = fields.Nested(ProductAction, required=False)
    
    slug = fields.Str(required=False)
    
