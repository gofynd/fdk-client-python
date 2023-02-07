"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .PaymentModeInfo import PaymentModeInfo











from .Prices import Prices





from .UserDataInfo import UserDataInfo







from .BagUnit import BagUnit





from .ShipmentStatus import ShipmentStatus



from .ShipmentItemFulFillingStore import ShipmentItemFulFillingStore



class ShipmentItem(BaseSchema):
    #  swagger.json

    
    payment_methods = fields.Dict(required=False)
    
    sla = fields.Dict(required=False)
    
    payment_mode_info = fields.Nested(PaymentModeInfo, required=False)
    
    fulfilling_centre = fields.Str(required=False)
    
    shipment_created_at = fields.Int(required=False)
    
    total_bags_count = fields.Int(required=False)
    
    total_shipments_in_order = fields.Int(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    id = fields.Str(required=False)
    
    user = fields.Nested(UserDataInfo, required=False)
    
    channel = fields.Dict(required=False)
    
    application = fields.Dict(required=False)
    
    bags = fields.List(fields.Nested(BagUnit, required=False), required=False)
    
    created_at = fields.Str(required=False)
    
    shipment_status = fields.Nested(ShipmentStatus, required=False)
    
    fulfilling_store = fields.Nested(ShipmentItemFulFillingStore, required=False)
    
