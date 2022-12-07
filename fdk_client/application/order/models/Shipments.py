"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












from .ShipmentTotalDetails import ShipmentTotalDetails











from .Promise import Promise











from .ShipmentPayment import ShipmentPayment





from .DeliveryAddress import DeliveryAddress



from .FulfillingCompany import FulfillingCompany





from .Prices import Prices





from .BreakupValues import BreakupValues







from .FulfillingStore import FulfillingStore







from .Bags import Bags



from .ShipmentUserInfo import ShipmentUserInfo



from .Invoice import Invoice





from .ShipmentStatus import ShipmentStatus







from .TrackingDetails import TrackingDetails



class Shipments(BaseSchema):
    #  swagger.json

    
    dp_name = fields.Str(required=False)
    
    traking_no = fields.Str(required=False)
    
    need_help_url = fields.Str(required=False)
    
    total_bags = fields.Int(required=False)
    
    total_details = fields.Nested(ShipmentTotalDetails, required=False)
    
    track_url = fields.Str(required=False)
    
    beneficiary_details = fields.Boolean(required=False)
    
    shipment_created_at = fields.Str(required=False)
    
    order_type = fields.Str(required=False)
    
    promise = fields.Nested(Promise, required=False)
    
    show_track_link = fields.Boolean(required=False)
    
    can_break = fields.Dict(required=False)
    
    returnable_date = fields.Str(required=False)
    
    can_return = fields.Boolean(required=False)
    
    payment = fields.Nested(ShipmentPayment, required=False)
    
    refund_details = fields.Dict(required=False)
    
    delivery_address = fields.Nested(DeliveryAddress, required=False)
    
    fulfilling_company = fields.Nested(FulfillingCompany, required=False)
    
    size_info = fields.Dict(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    delivery_date = fields.Str(required=False)
    
    breakup_values = fields.List(fields.Nested(BreakupValues, required=False), required=False)
    
    show_download_invoice = fields.Boolean(required=False)
    
    custom_meta = fields.List(fields.Dict(required=False), required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    order_id = fields.Str(required=False)
    
    awb_no = fields.Str(required=False)
    
    bags = fields.List(fields.Nested(Bags, required=False), required=False)
    
    user_info = fields.Nested(ShipmentUserInfo, required=False)
    
    invoice = fields.Nested(Invoice, required=False)
    
    comment = fields.Str(required=False)
    
    shipment_status = fields.Nested(ShipmentStatus, required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    shipment_id = fields.Str(required=False)
    
    tracking_details = fields.List(fields.Nested(TrackingDetails, required=False), required=False)
    