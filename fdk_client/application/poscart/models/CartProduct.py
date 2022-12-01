"""poscart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ProductAction import ProductAction









from .ProductImage import ProductImage



from .BaseInfo import BaseInfo



from .CategoryInfo import CategoryInfo





class CartProduct(BaseSchema):
    #  swagger.json

    
    action = fields.Nested(ProductAction, required=False)
    
    type = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    images = fields.List(fields.Nested(ProductImage, required=False), required=False)
    
    brand = fields.Nested(BaseInfo, required=False)
    
    categories = fields.List(fields.Nested(CategoryInfo, required=False), required=False)
    
    slug = fields.Str(required=False)
    
