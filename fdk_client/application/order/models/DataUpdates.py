"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ProductsDataUpdates1 import ProductsDataUpdates1



from .EntitiesDataUpdates import EntitiesDataUpdates



class DataUpdates(BaseSchema):
    #  swagger.json

    
    products = fields.List(fields.Nested(ProductsDataUpdates1, required=False), required=False)
    
    entities = fields.List(fields.Nested(EntitiesDataUpdates, required=False), required=False)
    
