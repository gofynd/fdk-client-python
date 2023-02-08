"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .BreakupValues import BreakupValues



from .ShipmentUserInfo import ShipmentUserInfo



















from .FulfillingStore import FulfillingStore





from .Invoice import Invoice



from .DeliveryAddress import DeliveryAddress







from .FulfillingCompany import FulfillingCompany









from .TrackingDetails import TrackingDetails







from .ShipmentPayment import ShipmentPayment



from .ShipmentStatus import ShipmentStatus





from .ShipmentTotalDetails import ShipmentTotalDetails







from .Bags import Bags





from .Prices import Prices



from .Promise import Promise







class Shipments(BaseSchema):
    #  swagger.json

    
    breakup_values = fields.List(fields.Nested(BreakupValues, required=False), required=False)
    
    user_info = fields.Nested(ShipmentUserInfo, required=False)
    
    traking_no = fields.Str(required=False)
    
    show_track_link = fields.Boolean(required=False)
    
    custom_meta = fields.List(fields.Dict(required=False), required=False)
    
    size_info = fields.Dict(required=False)
    
    order_id = fields.Str(required=False)
    
    returnable_date = fields.Str(required=False)
    
    show_download_invoice = fields.Boolean(required=False)
    
    can_return = fields.Boolean(required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    beneficiary_details = fields.Boolean(required=False)
    
    invoice = fields.Nested(Invoice, required=False)
    
    delivery_address = fields.Nested(DeliveryAddress, required=False)
    
    track_url = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    fulfilling_company = fields.Nested(FulfillingCompany, required=False)
    
    comment = fields.Str(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    total_bags = fields.Int(required=False)
    
    tracking_details = fields.List(fields.Nested(TrackingDetails, required=False), required=False)
    
    order_type = fields.Str(required=False)
    
    can_break = fields.Dict(required=False)
    
    payment = fields.Nested(ShipmentPayment, required=False)
    
    shipment_status = fields.Nested(ShipmentStatus, required=False)
    
    dp_name = fields.Str(required=False)
    
    total_details = fields.Nested(ShipmentTotalDetails, required=False)
    
    refund_details = fields.Dict(required=False)
    
    need_help_url = fields.Str(required=False)
    
    bags = fields.List(fields.Nested(Bags, required=False), required=False)
    
    shipment_created_at = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    promise = fields.Nested(Promise, required=False)
    
    delivery_date = fields.Str(required=False)
    
    awb_no = fields.Str(required=False)
    
