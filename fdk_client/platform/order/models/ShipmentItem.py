"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Prices import Prices





from .BagUnit import BagUnit



from .PaymentModeInfo import PaymentModeInfo



from .ShipmentItemFulFillingStore import ShipmentItemFulFillingStore



from .UserDataInfo import UserDataInfo

















from .ShipmentStatus import ShipmentStatus







class ShipmentItem(BaseSchema):
    #  swagger.json

    
    prices = fields.Nested(Prices, required=False)
    
    channel = fields.Dict(required=False)
    
    bags = fields.List(fields.Nested(BagUnit, required=False), required=False)
    
    payment_mode_info = fields.Nested(PaymentModeInfo, required=False)
    
    fulfilling_store = fields.Nested(ShipmentItemFulFillingStore, required=False)
    
    user = fields.Nested(UserDataInfo, required=False)
    
    total_bags_count = fields.Int(required=False)
    
    payment_methods = fields.Dict(required=False)
    
    total_shipments_in_order = fields.Int(required=False)
    
    shipment_created_at = fields.Int(required=False)
    
    created_at = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    fulfilling_centre = fields.Str(required=False)
    
    shipment_status = fields.Nested(ShipmentStatus, required=False)
    
    sla = fields.Dict(required=False)
    
    application = fields.Dict(required=False)
    
