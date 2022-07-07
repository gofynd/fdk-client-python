"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .FulFillingStore import FulFillingStore

from .Channel import Channel

from .UserInfo import UserInfo

from .Prices import Prices







from .ShipmentStatus import ShipmentStatus

from .PaymentModeInfo import PaymentModeInfo

from .BagItem import BagItem





from .Application import Application




class ShipmentItem(BaseSchema):
    # Orders swagger.json

    
    sla = fields.Dict(required=False)
    
    fulfilling_store = fields.Nested(FulFillingStore, required=False)
    
    channel = fields.Nested(Channel, required=False)
    
    user = fields.Nested(UserInfo, required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    fulfilling_centre = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    shipment_status = fields.Nested(ShipmentStatus, required=False)
    
    payment_mode_info = fields.Nested(PaymentModeInfo, required=False)
    
    bags = fields.List(fields.Nested(BagItem, required=False), required=False)
    
    total_bags_count = fields.Int(required=False)
    
    total_shipments_in_order = fields.Int(required=False)
    
    application = fields.Nested(Application, required=False)
    
    shipment_created_at = fields.Int(required=False)
    

