"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ReasonsData import ReasonsData





from .DataUpdates import DataUpdates



from .Products import Products



class ShipmentsRequest(BaseSchema):
    #  swagger.json

    
    reasons = fields.Nested(ReasonsData, required=False)
    
    identifier = fields.Str(required=False)
    
    data_updates = fields.Nested(DataUpdates, required=False)
    
    products = fields.List(fields.Nested(Products, required=False), required=False)
    
