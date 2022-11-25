"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ShipmentItemFulFillingStore import ShipmentItemFulFillingStore





from .PaymentModeInfo import PaymentModeInfo







from .Prices import Prices

from .UserDataInfo import UserDataInfo







from .BagUnit import BagUnit



from .ShipmentStatus import ShipmentStatus


class ShipmentItem(BaseSchema):
    # Order swagger.json

    
    fulfilling_store = fields.Nested(ShipmentItemFulFillingStore, required=False)
    
    total_bags_count = fields.Int(required=False)
    
    fulfilling_centre = fields.Str(required=False)
    
    payment_mode_info = fields.Nested(PaymentModeInfo, required=False)
    
    created_at = fields.Str(required=False)
    
    total_shipments_in_order = fields.Int(required=False)
    
    id = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    user = fields.Nested(UserDataInfo, required=False)
    
    shipment_created_at = fields.Int(required=False)
    
    sla = fields.Dict(required=False)
    
    application = fields.Dict(required=False)
    
    bags = fields.List(fields.Nested(BagUnit, required=False), required=False)
    
    channel = fields.Dict(required=False)
    
    shipment_status = fields.Nested(ShipmentStatus, required=False)
    

