"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .DataUpdates import DataUpdates



from .Products import Products





from .ReasonsData import ReasonsData



class ShipmentsRequest(BaseSchema):
    #  swagger.json

    
    data_updates = fields.Nested(DataUpdates, required=False)
    
    products = fields.List(fields.Nested(Products, required=False), required=False)
    
    identifier = fields.Str(required=False)
    
    reasons = fields.Nested(ReasonsData, required=False)
    
