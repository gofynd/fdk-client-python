"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .BagUnit import BagUnit

from .PaymentModeInfo import PaymentModeInfo

from .ShipmentItemFulFillingStore import ShipmentItemFulFillingStore

from .ShipmentStatus import ShipmentStatus

















from .Prices import Prices



from .UserDataInfo import UserDataInfo




class ShipmentItem(BaseSchema):
    # Order swagger.json

    
    fulfilling_centre = fields.Str(required=False)
    
    bags = fields.List(fields.Nested(BagUnit, required=False), required=False)
    
    payment_mode_info = fields.Nested(PaymentModeInfo, required=False)
    
    fulfilling_store = fields.Nested(ShipmentItemFulFillingStore, required=False)
    
    shipment_status = fields.Nested(ShipmentStatus, required=False)
    
    shipment_id = fields.Str(required=False)
    
    total_shipments_in_order = fields.Int(required=False)
    
    shipment_created_at = fields.Str(required=False)
    
    channel = fields.Dict(required=False)
    
    sla = fields.Dict(required=False)
    
    payment_methods = fields.Dict(required=False)
    
    total_bags_count = fields.Int(required=False)
    
    application = fields.Dict(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    created_at = fields.Str(required=False)
    
    user = fields.Nested(UserDataInfo, required=False)
    
    id = fields.Str(required=False)
    

