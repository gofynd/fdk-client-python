"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .ShipmentItemFulFillingStore import ShipmentItemFulFillingStore

from .UserDataInfo import UserDataInfo



from .ShipmentStatus import ShipmentStatus



from .BagUnit import BagUnit

from .Prices import Prices







from .PaymentModeInfo import PaymentModeInfo




class ShipmentItem(BaseSchema):
    # Order swagger.json

    
    sla = fields.Dict(required=False)
    
    shipment_created_at = fields.Int(required=False)
    
    created_at = fields.Str(required=False)
    
    fulfilling_store = fields.Nested(ShipmentItemFulFillingStore, required=False)
    
    user = fields.Nested(UserDataInfo, required=False)
    
    application = fields.Dict(required=False)
    
    shipment_status = fields.Nested(ShipmentStatus, required=False)
    
    total_shipments_in_order = fields.Int(required=False)
    
    bags = fields.List(fields.Nested(BagUnit, required=False), required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    id = fields.Str(required=False)
    
    channel = fields.Dict(required=False)
    
    fulfilling_centre = fields.Str(required=False)
    
    payment_mode_info = fields.Nested(PaymentModeInfo, required=False)
    
    total_bags_count = fields.Int(required=False)
    

