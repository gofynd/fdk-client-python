"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ShipmentPayment1 import ShipmentPayment1













from .DeliveryAddress import DeliveryAddress





from .Bags1 import Bags1



from .Prices import Prices





from .Promise1 import Promise1



from .ShipmentStatus import ShipmentStatus



from .BreakupValues import BreakupValues



from .FulfillingStore import FulfillingStore





from .ShipmentUserInfo import ShipmentUserInfo







from .FulfillingCompany import FulfillingCompany







from .ShipmentTotalDetails import ShipmentTotalDetails



from .TrackingDetails1 import TrackingDetails1



















from .Invoice import Invoice







class Shipments1(BaseSchema):
    #  swagger.json

    
    payment = fields.Nested(ShipmentPayment1, required=False)
    
    refund_details = fields.Dict(required=False)
    
    beneficiary_details = fields.Boolean(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    show_track_link = fields.Boolean(required=False)
    
    traking_no = fields.Str(required=False)
    
    delivery_address = fields.Nested(DeliveryAddress, required=False)
    
    comment = fields.Str(required=False)
    
    bags = fields.List(fields.Nested(Bags1, required=False), required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    can_return = fields.Boolean(required=False)
    
    promise = fields.Nested(Promise1, required=False)
    
    shipment_status = fields.Nested(ShipmentStatus, required=False)
    
    breakup_values = fields.List(fields.Nested(BreakupValues, required=False), required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    order_id = fields.Str(required=False)
    
    user_info = fields.Nested(ShipmentUserInfo, required=False)
    
    total_bags = fields.Int(required=False)
    
    track_url = fields.Str(required=False)
    
    fulfilling_company = fields.Nested(FulfillingCompany, required=False)
    
    awb_no = fields.Str(required=False)
    
    can_break = fields.Dict(required=False)
    
    total_details = fields.Nested(ShipmentTotalDetails, required=False)
    
    tracking_details = fields.List(fields.Nested(TrackingDetails1, required=False), required=False)
    
    custom_meta = fields.List(fields.Dict(required=False), required=False)
    
    shipment_id = fields.Str(required=False)
    
    returnable_date = fields.Str(required=False)
    
    show_download_invoice = fields.Boolean(required=False)
    
    need_help_url = fields.Str(required=False)
    
    shipment_created_at = fields.Str(required=False)
    
    order_type = fields.Str(required=False)
    
    size_info = fields.Dict(required=False)
    
    invoice = fields.Nested(Invoice, required=False)
    
    delivery_date = fields.Str(required=False)
    
    dp_name = fields.Str(required=False)
    
