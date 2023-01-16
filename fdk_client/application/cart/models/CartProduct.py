"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .CategoryInfo import CategoryInfo



from .ProductAction import ProductAction



from .BaseInfo import BaseInfo





from .NetQuantity import NetQuantity



from .ProductImage import ProductImage









class CartProduct(BaseSchema):
    #  swagger.json

    
    categories = fields.List(fields.Nested(CategoryInfo, required=False), required=False)
    
    action = fields.Nested(ProductAction, required=False)
    
    brand = fields.Nested(BaseInfo, required=False)
    
    slug = fields.Str(required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    images = fields.List(fields.Nested(ProductImage, required=False), required=False)
    
    type = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    