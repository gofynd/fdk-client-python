"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Prices import Prices



from .ShipmentStatus import ShipmentStatus

from .UserDataInfo import UserDataInfo















from .PaymentModeInfo import PaymentModeInfo



from .BagUnit import BagUnit

from .ShipmentItemFulFillingStore import ShipmentItemFulFillingStore




class ShipmentItem(BaseSchema):
    # Order swagger.json

    
    prices = fields.Nested(Prices, required=False)
    
    created_at = fields.Str(required=False)
    
    shipment_status = fields.Nested(ShipmentStatus, required=False)
    
    user = fields.Nested(UserDataInfo, required=False)
    
    payment_methods = fields.Dict(required=False)
    
    total_shipments_in_order = fields.Int(required=False)
    
    channel = fields.Dict(required=False)
    
    sla = fields.Dict(required=False)
    
    shipment_created_at = fields.Int(required=False)
    
    total_bags_count = fields.Int(required=False)
    
    id = fields.Str(required=False)
    
    payment_mode_info = fields.Nested(PaymentModeInfo, required=False)
    
    fulfilling_centre = fields.Str(required=False)
    
    bags = fields.List(fields.Nested(BagUnit, required=False), required=False)
    
    fulfilling_store = fields.Nested(ShipmentItemFulFillingStore, required=False)
    
    application = fields.Dict(required=False)
    

