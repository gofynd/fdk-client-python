"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Prices import Prices

from .UserDataInfo import UserDataInfo



from .PaymentModeInfo import PaymentModeInfo









from .ShipmentStatus import ShipmentStatus



from .FulFillingStore import FulFillingStore

from .BagUnit import BagUnit








class ShipmentItem(BaseSchema):
    # Orders swagger.json

    
    prices = fields.Nested(Prices, required=False)
    
    user = fields.Nested(UserDataInfo, required=False)
    
    shipment_created_at = fields.Int(required=False)
    
    payment_mode_info = fields.Nested(PaymentModeInfo, required=False)
    
    total_bags_count = fields.Int(required=False)
    
    fulfilling_centre = fields.Str(required=False)
    
    total_shipments_in_order = fields.Int(required=False)
    
    channel = fields.Dict(required=False)
    
    shipment_status = fields.Nested(ShipmentStatus, required=False)
    
    sla = fields.Dict(required=False)
    
    fulfilling_store = fields.Nested(FulFillingStore, required=False)
    
    bags = fields.List(fields.Nested(BagUnit, required=False), required=False)
    
    created_at = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    application = fields.Dict(required=False)
    

