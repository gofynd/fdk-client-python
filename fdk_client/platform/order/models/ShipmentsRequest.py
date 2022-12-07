"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .DataUpdates import DataUpdates



from .Products import Products





class ShipmentsRequest(BaseSchema):
    #  swagger.json

    
    data_updates = fields.Nested(DataUpdates, required=False)
    
    products = fields.List(fields.Nested(Products, required=False), required=False)
    
    reasons = fields.List(fields.Dict(required=False), required=False)
    
