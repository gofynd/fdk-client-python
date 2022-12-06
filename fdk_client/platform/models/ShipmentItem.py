"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PaymentModeInfo import PaymentModeInfo









from .Prices import Prices

from .ShipmentStatus import ShipmentStatus

from .BagUnit import BagUnit





from .UserDataInfo import UserDataInfo



from .ShipmentItemFulFillingStore import ShipmentItemFulFillingStore






class ShipmentItem(BaseSchema):
    # Order swagger.json

    
    payment_mode_info = fields.Nested(PaymentModeInfo, required=False)
    
    total_shipments_in_order = fields.Int(required=False)
    
    shipment_created_at = fields.Int(required=False)
    
    application = fields.Dict(required=False)
    
    sla = fields.Dict(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    shipment_status = fields.Nested(ShipmentStatus, required=False)
    
    bags = fields.List(fields.Nested(BagUnit, required=False), required=False)
    
    total_bags_count = fields.Int(required=False)
    
    id = fields.Str(required=False)
    
    user = fields.Nested(UserDataInfo, required=False)
    
    channel = fields.Dict(required=False)
    
    fulfilling_store = fields.Nested(ShipmentItemFulFillingStore, required=False)
    
    created_at = fields.Str(required=False)
    
    fulfilling_centre = fields.Str(required=False)
    

