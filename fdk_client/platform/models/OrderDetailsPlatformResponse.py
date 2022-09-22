"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .ShipmentPrices1 import ShipmentPrices1

from .RtoAddress1 import RtoAddress1



from .ShipmentProduct import ShipmentProduct





from .ShipmentStatusCommon import ShipmentStatusCommon







from .RequestedDPConfs import RequestedDPConfs





from .UserObj import UserObj

from .ShipmentInvoice1 import ShipmentInvoice1





from .Brand import Brand











from .AffiliateDetails import AffiliateDetails







from .ShipmentPayments import ShipmentPayments

from .Store1 import Store1









from .ShipmentDetails1 import ShipmentDetails1

from .CurrentShipmentStatus import CurrentShipmentStatus

from .Bag import Bag









from .OrderObj import OrderObj

from .Company1 import Company1

from .EinvoiceInfo import EinvoiceInfo

from .Store1 import Store1











from .ShipmentGst1 import ShipmentGst1



from .DpDetails1 import DpDetails1

from .DeliveryAddress import DeliveryAddress

from .BagStatusHistory import BagStatusHistory


class OrderDetailsPlatformResponse(BaseSchema):
    # Order swagger.json

    
    journey_type = fields.Str(required=False)
    
    shipment_value = fields.Float(required=False)
    
    prices = fields.Nested(ShipmentPrices1, required=False)
    
    rto_address = fields.Nested(RtoAddress1, required=False)
    
    transaction_type = fields.Str(required=False)
    
    products = fields.List(fields.Nested(ShipmentProduct, required=False), required=False)
    
    qc_required = fields.Raw(required=False)
    
    order_integration_id = fields.Str(required=False)
    
    shipment_status_history = fields.List(fields.Nested(ShipmentStatusCommon, required=False), required=False)
    
    weight = fields.Dict(required=False)
    
    operational_status = fields.Str(required=False)
    
    payment_type = fields.Str(required=False)
    
    requested_dp_conf = fields.Nested(RequestedDPConfs, required=False)
    
    fyndstore_emp = fields.Dict(required=False)
    
    restore_promos = fields.Dict(required=False)
    
    user = fields.Nested(UserObj, required=False)
    
    invoice = fields.Nested(ShipmentInvoice1, required=False)
    
    search_key = fields.Dict(required=False)
    
    total_shipment_bags = fields.Int(required=False)
    
    brand = fields.Nested(Brand, required=False)
    
    order_type = fields.Str(required=False)
    
    coupon = fields.Dict(required=False)
    
    shipment_id = fields.Str(required=False)
    
    s_id = fields.Str(required=False)
    
    order_value = fields.Float(required=False)
    
    affiliate_details = fields.Nested(AffiliateDetails, required=False)
    
    no_of_bags_order = fields.Int(required=False)
    
    restore_coupon = fields.Boolean(required=False)
    
    lock_status = fields.Boolean(required=False)
    
    payments = fields.Nested(ShipmentPayments, required=False)
    
    ordering_store = fields.Nested(Store1, required=False)
    
    cart_id = fields.Int(required=False)
    
    total_shipments_in_order = fields.Int(required=False)
    
    article_details = fields.Dict(required=False)
    
    order_source = fields.Str(required=False)
    
    shipment = fields.Nested(ShipmentDetails1, required=False)
    
    shipment_status = fields.Nested(CurrentShipmentStatus, required=False)
    
    bags = fields.List(fields.Nested(Bag, required=False), required=False)
    
    comment = fields.Str(required=False)
    
    delivery_slot = fields.Dict(required=False)
    
    app_id = fields.Str(required=False)
    
    is_processing = fields.Boolean(required=False)
    
    order = fields.Nested(OrderObj, required=False)
    
    company = fields.Nested(Company1, required=False)
    
    einvoice_info = fields.Nested(EinvoiceInfo, required=False)
    
    fulfilling_store = fields.Nested(Store1, required=False)
    
    payment_methods = fields.Dict(required=False)
    
    shipment_quantity = fields.Int(required=False)
    
    shipment_update_time = fields.Float(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    original_bag_list = fields.List(fields.Int(required=False), required=False)
    
    shipment_gst = fields.Nested(ShipmentGst1, required=False)
    
    fallback_user = fields.Dict(required=False)
    
    dp_details = fields.Nested(DpDetails1, required=False)
    
    delivery_address = fields.Nested(DeliveryAddress, required=False)
    
    bag_status_history = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    

