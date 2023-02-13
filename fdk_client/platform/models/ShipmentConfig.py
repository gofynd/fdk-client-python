"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .LocationDetails import LocationDetails

from .ShipmentDetails import ShipmentDetails










class ShipmentConfig(BaseSchema):
    # OrderManage swagger.json

    
    to_pincode = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    location_details = fields.Nested(LocationDetails, required=False)
    
    shipment = fields.List(fields.Nested(ShipmentDetails, required=False), required=False)
    
    journey = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
