"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .EntitiesReasons import EntitiesReasons



from .ProductsReasons import ProductsReasons



class ReasonsData(BaseSchema):
    #  swagger.json

    
    entities = fields.List(fields.Nested(EntitiesReasons, required=False), required=False)
    
    products = fields.List(fields.Nested(ProductsReasons, required=False), required=False)
    
