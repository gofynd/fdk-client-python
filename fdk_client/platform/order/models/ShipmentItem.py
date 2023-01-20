"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .BagUnit import BagUnit





from .ShipmentStatus import ShipmentStatus















from .UserDataInfo import UserDataInfo



from .ShipmentItemFulFillingStore import ShipmentItemFulFillingStore



from .Prices import Prices



from .PaymentModeInfo import PaymentModeInfo





class ShipmentItem(BaseSchema):
    #  swagger.json

    
    total_bags_count = fields.Int(required=False)
    
    channel = fields.Dict(required=False)
    
    bags = fields.List(fields.Nested(BagUnit, required=False), required=False)
    
    sla = fields.Dict(required=False)
    
    shipment_status = fields.Nested(ShipmentStatus, required=False)
    
    payment_methods = fields.Dict(required=False)
    
    id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    application = fields.Dict(required=False)
    
    shipment_created_at = fields.Int(required=False)
    
    fulfilling_centre = fields.Str(required=False)
    
    user = fields.Nested(UserDataInfo, required=False)
    
    fulfilling_store = fields.Nested(ShipmentItemFulFillingStore, required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    payment_mode_info = fields.Nested(PaymentModeInfo, required=False)
    
    total_shipments_in_order = fields.Int(required=False)
    
