"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ShipmentStatus import ShipmentStatus



from .ShipmentItemFulFillingStore import ShipmentItemFulFillingStore

from .UserDataInfo import UserDataInfo











from .BagUnit import BagUnit

from .PaymentModeInfo import PaymentModeInfo





from .Prices import Prices




class ShipmentItem(BaseSchema):
    # Order swagger.json

    
    total_bags_count = fields.Int(required=False)
    
    shipment_status = fields.Nested(ShipmentStatus, required=False)
    
    application = fields.Dict(required=False)
    
    fulfilling_store = fields.Nested(ShipmentItemFulFillingStore, required=False)
    
    user = fields.Nested(UserDataInfo, required=False)
    
    sla = fields.Dict(required=False)
    
    payment_methods = fields.Dict(required=False)
    
    total_shipments_in_order = fields.Int(required=False)
    
    fulfilling_centre = fields.Str(required=False)
    
    shipment_created_at = fields.Int(required=False)
    
    bags = fields.List(fields.Nested(BagUnit, required=False), required=False)
    
    payment_mode_info = fields.Nested(PaymentModeInfo, required=False)
    
    channel = fields.Dict(required=False)
    
    id = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    created_at = fields.Str(required=False)
    

