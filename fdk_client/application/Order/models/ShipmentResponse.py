"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .Prices import Prices







from .InvoiceData import InvoiceData



from .UserInfo1 import UserInfo1



from .DeliveryAddress import DeliveryAddress











from .BagsData import BagsData











from .PaymentInfo import PaymentInfo





from .Promise1 import Promise1



from .FulfillingCompany import FulfillingCompany





from .ShipmentStatus import ShipmentStatus











from .PricesBreakup import PricesBreakup



from .TrackingDetails import TrackingDetails





from .ShipmentTotalDetails1 import ShipmentTotalDetails1













from .FulfillingStore import FulfillingStore



class ShipmentResponse(BaseSchema):
    #  swagger.json

    
    prices = fields.Nested(Prices, required=False)
    
    show_track_link = fields.Boolean(required=False)
    
    shipment_id = fields.Str(required=False)
    
    invoice = fields.Nested(InvoiceData, required=False)
    
    user_info = fields.Nested(UserInfo1, required=False)
    
    delivery_address = fields.Nested(DeliveryAddress, required=False)
    
    dp_name = fields.Str(required=False)
    
    refund_details = fields.Dict(required=False)
    
    order_type = fields.Str(required=False)
    
    beneficiary_details = fields.Boolean(required=False)
    
    bags = fields.List(fields.Nested(BagsData, required=False), required=False)
    
    can_break = fields.Dict(required=False)
    
    can_return = fields.Boolean(required=False)
    
    show_download_invoice = fields.Boolean(required=False)
    
    track_url = fields.Str(required=False)
    
    payment = fields.Nested(PaymentInfo, required=False)
    
    custom_meta = fields.List(fields.Dict(required=False), required=False)
    
    promise = fields.Nested(Promise1, required=False)
    
    fulfilling_company = fields.Nested(FulfillingCompany, required=False)
    
    size_info = fields.Dict(required=False)
    
    shipment_status = fields.Nested(ShipmentStatus, required=False)
    
    order_id = fields.Str(required=False)
    
    shipment_created_at = fields.Str(required=False)
    
    awb_no = fields.Str(required=False)
    
    need_help_url = fields.Str(required=False)
    
    breakup_values = fields.List(fields.Nested(PricesBreakup, required=False), required=False)
    
    tracking_details = fields.List(fields.Nested(TrackingDetails, required=False), required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    total_details = fields.Nested(ShipmentTotalDetails1, required=False)
    
    traking_no = fields.Str(required=False)
    
    returnable_date = fields.Str(required=False)
    
    delivery_date = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    total_bags = fields.Int(required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
