"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ProductAction import ProductAction







from .BaseInfo import BaseInfo







from .NetQuantity import NetQuantity



from .CategoryInfo import CategoryInfo



from .ProductImage import ProductImage



class CartProduct(BaseSchema):
    #  swagger.json

    
    action = fields.Nested(ProductAction, required=False)
    
    type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    brand = fields.Nested(BaseInfo, required=False)
    
    slug = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    categories = fields.List(fields.Nested(CategoryInfo, required=False), required=False)
    
    images = fields.List(fields.Nested(ProductImage, required=False), required=False)
    
