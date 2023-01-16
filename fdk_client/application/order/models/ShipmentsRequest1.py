"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .Products1 import Products1



from .ReasonsData1 import ReasonsData1



from .DataUpdates import DataUpdates



class ShipmentsRequest1(BaseSchema):
    #  swagger.json

    
    identifier = fields.Str(required=False)
    
    products = fields.List(fields.Nested(Products1, required=False), required=False)
    
    reasons = fields.Nested(ReasonsData1, required=False)
    
    data_updates = fields.Nested(DataUpdates, required=False)
    
