"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ProductAction import ProductAction



from .CategoryInfo import CategoryInfo









from .BaseInfo import BaseInfo



from .ProductImage import ProductImage





class CartProduct(BaseSchema):
    #  swagger.json

    
    action = fields.Nested(ProductAction, required=False)
    
    categories = fields.List(fields.Nested(CategoryInfo, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    brand = fields.Nested(BaseInfo, required=False)
    
    images = fields.List(fields.Nested(ProductImage, required=False), required=False)
    
    slug = fields.Str(required=False)
    
