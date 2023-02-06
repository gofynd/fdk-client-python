"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ProductsDataUpdates import ProductsDataUpdates



from .EntitiesDataUpdates import EntitiesDataUpdates



class DataUpdates(BaseSchema):
    #  swagger.json

    
    products = fields.List(fields.Nested(ProductsDataUpdates, required=False), required=False)
    
    entities = fields.List(fields.Nested(EntitiesDataUpdates, required=False), required=False)
    
