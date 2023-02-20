"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .Products import Products



from .ReasonsData import ReasonsData



from .DataUpdates import DataUpdates



class ShipmentsRequest(BaseSchema):
    #  swagger.json

    
    identifier = fields.Str(required=False)
    
    products = fields.List(fields.Nested(Products, required=False), required=False)
    
    reasons = fields.Nested(ReasonsData, required=False)
    
    data_updates = fields.Nested(DataUpdates, required=False)
    
