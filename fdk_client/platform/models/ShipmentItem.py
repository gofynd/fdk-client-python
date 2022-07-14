"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .BagUnit import BagUnit

from .UserDataInfo import UserDataInfo





from .Prices import Prices



from .ShipmentItemFulFillingStore import ShipmentItemFulFillingStore





from .ShipmentStatus import ShipmentStatus

from .PaymentModeInfo import PaymentModeInfo










class ShipmentItem(BaseSchema):
    # Orders swagger.json

    
    bags = fields.List(fields.Nested(BagUnit, required=False), required=False)
    
    user = fields.Nested(UserDataInfo, required=False)
    
    total_shipments_in_order = fields.Int(required=False)
    
    application = fields.Dict(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    shipment_created_at = fields.Int(required=False)
    
    fulfilling_store = fields.Nested(ShipmentItemFulFillingStore, required=False)
    
    total_bags_count = fields.Int(required=False)
    
    fulfilling_centre = fields.Str(required=False)
    
    shipment_status = fields.Nested(ShipmentStatus, required=False)
    
    payment_mode_info = fields.Nested(PaymentModeInfo, required=False)
    
    created_at = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    sla = fields.Dict(required=False)
    
    channel = fields.Dict(required=False)
    

