"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ReasonsData import ReasonsData



from .Products import Products



from .DataUpdates import DataUpdates





class ShipmentsRequest(BaseSchema):
    #  swagger.json

    
    reasons = fields.Nested(ReasonsData, required=False)
    
    products = fields.List(fields.Nested(Products, required=False), required=False)
    
    data_updates = fields.Nested(DataUpdates, required=False)
    
    identifier = fields.Str(required=False)
    
