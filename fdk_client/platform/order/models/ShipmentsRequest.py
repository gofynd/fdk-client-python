"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Products import Products



from .ReasonsData import ReasonsData





from .DataUpdates import DataUpdates



class ShipmentsRequest(BaseSchema):
    #  swagger.json

    
    products = fields.List(fields.Nested(Products, required=False), required=False)
    
    reasons = fields.Nested(ReasonsData, required=False)
    
    identifier = fields.Str(required=False)
    
    data_updates = fields.Nested(DataUpdates, required=False)
    
