"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .Prices import Prices





from .PaymentModeInfo import PaymentModeInfo

from .UserDataInfo import UserDataInfo







from .BagUnit import BagUnit

from .ShipmentItemFulFillingStore import ShipmentItemFulFillingStore









from .ShipmentStatus import ShipmentStatus


class ShipmentItem(BaseSchema):
    # Order swagger.json

    
    channel = fields.Dict(required=False)
    
    total_shipments_in_order = fields.Int(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    total_bags_count = fields.Int(required=False)
    
    id = fields.Str(required=False)
    
    payment_mode_info = fields.Nested(PaymentModeInfo, required=False)
    
    user = fields.Nested(UserDataInfo, required=False)
    
    created_at = fields.Str(required=False)
    
    payment_methods = fields.Dict(required=False)
    
    shipment_id = fields.Str(required=False)
    
    bags = fields.List(fields.Nested(BagUnit, required=False), required=False)
    
    fulfilling_store = fields.Nested(ShipmentItemFulFillingStore, required=False)
    
    shipment_created_at = fields.Str(required=False)
    
    sla = fields.Dict(required=False)
    
    fulfilling_centre = fields.Str(required=False)
    
    application = fields.Dict(required=False)
    
    shipment_status = fields.Nested(ShipmentStatus, required=False)
    

