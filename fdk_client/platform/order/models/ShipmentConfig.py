"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












from .ShipmentDetails import ShipmentDetails



from .LocationDetails import LocationDetails







class ShipmentConfig(BaseSchema):
    #  swagger.json

    
    identifier = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    shipment = fields.List(fields.Nested(ShipmentDetails, required=False), required=False)
    
    location_details = fields.Nested(LocationDetails, required=False)
    
    to_pincode = fields.Str(required=False)
    
    journey = fields.Str(required=False)
    
