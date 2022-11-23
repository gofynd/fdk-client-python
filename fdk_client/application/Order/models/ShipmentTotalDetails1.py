"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class ShipmentTotalDetails1(BaseSchema):
    #  swagger.json

    
    total_price = fields.Float(required=False)
    
    pieces = fields.Float(required=False)
    
    sizes = fields.Float(required=False)
    
