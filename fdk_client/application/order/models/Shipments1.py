"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .FulfillingStore import FulfillingStore













from .Bags1 import Bags1



from .ShipmentStatus import ShipmentStatus





from .ShipmentTotalDetails import ShipmentTotalDetails



from .Prices import Prices



from .Promise1 import Promise1





















from .ShipmentUserInfo import ShipmentUserInfo







from .DeliveryAddress import DeliveryAddress



from .FulfillingCompany import FulfillingCompany





from .Invoice import Invoice





from .TrackingDetails1 import TrackingDetails1



from .BreakupValues import BreakupValues







from .ShipmentPayment1 import ShipmentPayment1





class Shipments1(BaseSchema):
    #  swagger.json

    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    returnable_date = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    track_url = fields.Str(required=False)
    
    custom_meta = fields.List(fields.Dict(required=False), required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    bags = fields.List(fields.Nested(Bags1, required=False), required=False)
    
    shipment_status = fields.Nested(ShipmentStatus, required=False)
    
    traking_no = fields.Str(required=False)
    
    total_details = fields.Nested(ShipmentTotalDetails, required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    promise = fields.Nested(Promise1, required=False)
    
    can_break = fields.Dict(required=False)
    
    shipment_created_at = fields.Str(required=False)
    
    need_help_url = fields.Str(required=False)
    
    beneficiary_details = fields.Boolean(required=False)
    
    show_download_invoice = fields.Boolean(required=False)
    
    can_return = fields.Boolean(required=False)
    
    refund_details = fields.Dict(required=False)
    
    total_bags = fields.Int(required=False)
    
    delivery_date = fields.Str(required=False)
    
    user_info = fields.Nested(ShipmentUserInfo, required=False)
    
    comment = fields.Str(required=False)
    
    size_info = fields.Dict(required=False)
    
    delivery_address = fields.Nested(DeliveryAddress, required=False)
    
    fulfilling_company = fields.Nested(FulfillingCompany, required=False)
    
    shipment_id = fields.Str(required=False)
    
    invoice = fields.Nested(Invoice, required=False)
    
    awb_no = fields.Str(required=False)
    
    tracking_details = fields.List(fields.Nested(TrackingDetails1, required=False), required=False)
    
    breakup_values = fields.List(fields.Nested(BreakupValues, required=False), required=False)
    
    order_type = fields.Str(required=False)
    
    show_track_link = fields.Boolean(required=False)
    
    payment = fields.Nested(ShipmentPayment1, required=False)
    
    dp_name = fields.Str(required=False)
    
