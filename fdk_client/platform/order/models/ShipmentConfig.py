"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .LocationDetails import LocationDetails





from .ShipmentDetails import ShipmentDetails







class ShipmentConfig(BaseSchema):
    #  swagger.json

    
    action = fields.Str(required=False)
    
    to_pincode = fields.Str(required=False)
    
    journey = fields.Str(required=False)
    
    location_details = fields.Nested(LocationDetails, required=False)
    
    identifier = fields.Str(required=False)
    
    shipment = fields.List(fields.Nested(ShipmentDetails, required=False), required=False)
    
    payment_mode = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
