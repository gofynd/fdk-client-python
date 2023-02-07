"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Product import Product



class SingleProductResponse(BaseSchema):
    #  swagger.json

    
    data = fields.Nested(Product, required=False)
    
