"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ReasonsData import ReasonsData



from .Products import Products





from .DataUpdates1 import DataUpdates1



class ShipmentsRequest(BaseSchema):
    #  swagger.json

    
    reasons = fields.Nested(ReasonsData, required=False)
    
    products = fields.List(fields.Nested(Products, required=False), required=False)
    
    identifier = fields.Str(required=False)
    
    data_updates = fields.Nested(DataUpdates1, required=False)
    
