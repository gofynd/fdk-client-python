"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .ShipmentItemFulFillingStore import ShipmentItemFulFillingStore

from .PaymentModeInfo import PaymentModeInfo









from .ShipmentStatus import ShipmentStatus



from .Prices import Prices



from .UserDataInfo import UserDataInfo



from .BagUnit import BagUnit


class ShipmentItem(BaseSchema):
    # Order swagger.json

    
    created_at = fields.Str(required=False)
    
    fulfilling_centre = fields.Str(required=False)
    
    shipment_created_at = fields.Int(required=False)
    
    fulfilling_store = fields.Nested(ShipmentItemFulFillingStore, required=False)
    
    payment_mode_info = fields.Nested(PaymentModeInfo, required=False)
    
    sla = fields.Dict(required=False)
    
    channel = fields.Dict(required=False)
    
    total_shipments_in_order = fields.Int(required=False)
    
    total_bags_count = fields.Int(required=False)
    
    shipment_status = fields.Nested(ShipmentStatus, required=False)
    
    payment_methods = fields.Dict(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    id = fields.Str(required=False)
    
    user = fields.Nested(UserDataInfo, required=False)
    
    application = fields.Dict(required=False)
    
    bags = fields.List(fields.Nested(BagUnit, required=False), required=False)
    

