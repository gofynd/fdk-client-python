"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .EntitiesDataUpdates import EntitiesDataUpdates



from .ProductsDataUpdates import ProductsDataUpdates



class DataUpdates(BaseSchema):
    #  swagger.json

    
    entities = fields.List(fields.Nested(EntitiesDataUpdates, required=False), required=False)
    
    products = fields.List(fields.Nested(ProductsDataUpdates, required=False), required=False)
    
