"""poscart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .BaseInfo import BaseInfo





from .CategoryInfo import CategoryInfo







from .ProductImage import ProductImage



from .ProductAction import ProductAction





from .NetQuantity import NetQuantity



class CartProduct(BaseSchema):
    #  swagger.json

    
    brand = fields.Nested(BaseInfo, required=False)
    
    type = fields.Str(required=False)
    
    categories = fields.List(fields.Nested(CategoryInfo, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    images = fields.List(fields.Nested(ProductImage, required=False), required=False)
    
    action = fields.Nested(ProductAction, required=False)
    
    slug = fields.Str(required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
