"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class ShipmentTotalDetails(BaseSchema):
    #  swagger.json

    
    sizes = fields.Int(required=False)
    
    pieces = fields.Int(required=False)
    
    total_price = fields.Float(required=False)
    
