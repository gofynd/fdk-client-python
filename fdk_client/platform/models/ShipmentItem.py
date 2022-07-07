"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .PaymentModeInfo import PaymentModeInfo





from .UserInfo import UserInfo

from .ShipmentStatus import ShipmentStatus



from .FulFillingStore import FulFillingStore



from .BagItem import BagItem

from .Channel import Channel

from .Prices import Prices

from .Application import Application


class ShipmentItem(BaseSchema):
    # Orders swagger.json

    
    total_bags_count = fields.Int(required=False)
    
    shipment_created_at = fields.Int(required=False)
    
    sla = fields.Dict(required=False)
    
    payment_mode_info = fields.Nested(PaymentModeInfo, required=False)
    
    id = fields.Str(required=False)
    
    total_shipments_in_order = fields.Int(required=False)
    
    user = fields.Nested(UserInfo, required=False)
    
    shipment_status = fields.Nested(ShipmentStatus, required=False)
    
    created_at = fields.Str(required=False)
    
    fulfilling_store = fields.Nested(FulFillingStore, required=False)
    
    fulfilling_centre = fields.Str(required=False)
    
    bags = fields.List(fields.Nested(BagItem, required=False), required=False)
    
    channel = fields.Nested(Channel, required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    application = fields.Nested(Application, required=False)
    

