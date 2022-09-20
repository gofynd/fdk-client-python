"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Prices import Prices

from .ShipmentStatus import ShipmentStatus







from .UserDataInfo import UserDataInfo



from .BagUnit import BagUnit









from .PaymentModeInfo import PaymentModeInfo



from .ShipmentItemFulFillingStore import ShipmentItemFulFillingStore


class ShipmentItem(BaseSchema):
    # Orders swagger.json

    
    prices = fields.Nested(Prices, required=False)
    
    shipment_status = fields.Nested(ShipmentStatus, required=False)
    
    total_bags_count = fields.Int(required=False)
    
    shipment_created_at = fields.Int(required=False)
    
    created_at = fields.Str(required=False)
    
    user = fields.Nested(UserDataInfo, required=False)
    
    fulfilling_centre = fields.Str(required=False)
    
    bags = fields.List(fields.Nested(BagUnit, required=False), required=False)
    
    channel = fields.Dict(required=False)
    
    application = fields.Dict(required=False)
    
    total_shipments_in_order = fields.Int(required=False)
    
    sla = fields.Dict(required=False)
    
    payment_mode_info = fields.Nested(PaymentModeInfo, required=False)
    
    id = fields.Str(required=False)
    
    fulfilling_store = fields.Nested(ShipmentItemFulFillingStore, required=False)
    

