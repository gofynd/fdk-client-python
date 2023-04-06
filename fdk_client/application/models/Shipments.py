"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Bags import Bags











from .Prices import Prices





from .DeliveryAddress import DeliveryAddress









from .FulfillingStore import FulfillingStore

from .TrackingDetails import TrackingDetails

from .ShipmentPayment import ShipmentPayment

from .ShipmentUserInfo import ShipmentUserInfo





from .FulfillingCompany import FulfillingCompany

from .BreakupValues import BreakupValues





from .ShipmentTotalDetails import ShipmentTotalDetails

from .ShipmentStatus import ShipmentStatus









from .Promise import Promise



from .Invoice import Invoice




class Shipments(BaseSchema):
    # Order swagger.json

    
    awb_no = fields.Str(required=False)
    
    bags = fields.List(fields.Nested(Bags, required=False), required=False)
    
    refund_details = fields.Dict(required=False)
    
    track_url = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    need_help_url = fields.Str(required=False)
    
    beneficiary_details = fields.Boolean(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    show_download_invoice = fields.Boolean(required=False)
    
    shipment_created_at = fields.Str(required=False)
    
    delivery_address = fields.Nested(DeliveryAddress, required=False)
    
    can_return = fields.Boolean(required=False)
    
    show_track_link = fields.Boolean(required=False)
    
    size_info = fields.Dict(required=False)
    
    order_type = fields.Str(required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    tracking_details = fields.List(fields.Nested(TrackingDetails, required=False), required=False)
    
    payment = fields.Nested(ShipmentPayment, required=False)
    
    user_info = fields.Nested(ShipmentUserInfo, required=False)
    
    can_break = fields.Dict(required=False)
    
    returnable_date = fields.Str(required=False)
    
    fulfilling_company = fields.Nested(FulfillingCompany, required=False)
    
    breakup_values = fields.List(fields.Nested(BreakupValues, required=False), required=False)
    
    delivery_date = fields.Str(required=False)
    
    total_bags = fields.Int(required=False)
    
    total_details = fields.Nested(ShipmentTotalDetails, required=False)
    
    shipment_status = fields.Nested(ShipmentStatus, required=False)
    
    dp_name = fields.Str(required=False)
    
    traking_no = fields.Str(required=False)
    
    custom_meta = fields.List(fields.Dict(required=False), required=False)
    
    order_id = fields.Str(required=False)
    
    promise = fields.Nested(Promise, required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    invoice = fields.Nested(Invoice, required=False)
    
    shipment_id = fields.Str(required=False)
    

