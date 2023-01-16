"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ProductsDataUpdates import ProductsDataUpdates



from .EntitiesDataUpdates import EntitiesDataUpdates



class DataUpdates1(BaseSchema):
    #  swagger.json

    
    products = fields.List(fields.Nested(ProductsDataUpdates, required=False), required=False)
    
    entities = fields.List(fields.Nested(EntitiesDataUpdates, required=False), required=False)
    
