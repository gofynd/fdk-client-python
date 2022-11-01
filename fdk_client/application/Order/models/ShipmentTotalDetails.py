"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class ShipmentTotalDetails(BaseSchema):
    #  swagger.json

    
    total_price = fields.Float(required=False)
    
    sizes = fields.Int(required=False)
    
    pieces = fields.Int(required=False)
    
