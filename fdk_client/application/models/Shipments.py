"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .DeliveryAddress import DeliveryAddress





from .Promise import Promise



from .FulfillingCompany import FulfillingCompany



from .ShipmentStatus import ShipmentStatus





from .BreakupValues import BreakupValues











from .ShipmentTotalDetails import ShipmentTotalDetails







from .Bags import Bags



from .ShipmentUserInfo import ShipmentUserInfo

from .Invoice import Invoice

from .TrackingDetails import TrackingDetails







from .FulfillingStore import FulfillingStore









from .Prices import Prices

from .ShipmentPayment import ShipmentPayment


class Shipments(BaseSchema):
    # Order swagger.json

    
    delivery_address = fields.Nested(DeliveryAddress, required=False)
    
    custom_meta = fields.List(fields.Dict(required=False), required=False)
    
    need_help_url = fields.Str(required=False)
    
    promise = fields.Nested(Promise, required=False)
    
    order_type = fields.Str(required=False)
    
    fulfilling_company = fields.Nested(FulfillingCompany, required=False)
    
    refund_details = fields.Dict(required=False)
    
    shipment_status = fields.Nested(ShipmentStatus, required=False)
    
    delivery_date = fields.Str(required=False)
    
    track_url = fields.Str(required=False)
    
    breakup_values = fields.List(fields.Nested(BreakupValues, required=False), required=False)
    
    show_download_invoice = fields.Boolean(required=False)
    
    dp_name = fields.Str(required=False)
    
    shipment_created_at = fields.Str(required=False)
    
    total_bags = fields.Int(required=False)
    
    can_return = fields.Boolean(required=False)
    
    total_details = fields.Nested(ShipmentTotalDetails, required=False)
    
    can_break = fields.Dict(required=False)
    
    traking_no = fields.Str(required=False)
    
    beneficiary_details = fields.Boolean(required=False)
    
    bags = fields.List(fields.Nested(Bags, required=False), required=False)
    
    shipment_id = fields.Str(required=False)
    
    user_info = fields.Nested(ShipmentUserInfo, required=False)
    
    invoice = fields.Nested(Invoice, required=False)
    
    tracking_details = fields.List(fields.Nested(TrackingDetails, required=False), required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    show_track_link = fields.Boolean(required=False)
    
    size_info = fields.Dict(required=False)
    
    fulfilling_store = fields.Nested(FulfillingStore, required=False)
    
    order_id = fields.Str(required=False)
    
    returnable_date = fields.Str(required=False)
    
    awb_no = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    prices = fields.Nested(Prices, required=False)
    
    payment = fields.Nested(ShipmentPayment, required=False)
    

