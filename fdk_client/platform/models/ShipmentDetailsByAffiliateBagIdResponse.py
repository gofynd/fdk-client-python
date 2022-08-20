"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .EinvoiceInfo import EinvoiceInfo

from .RequestedDPConfs import RequestedDPConfs

from .ShipmentPayments import ShipmentPayments

from .CurrentShipmentStatus import CurrentShipmentStatus





from .BagStatusHistory import BagStatusHistory

from .UserObj import UserObj

from .AffiliateDetails import AffiliateDetails





from .ShipmentInvoice1 import ShipmentInvoice1









from .RtoAddress1 import RtoAddress1

from .ShipmentGst1 import ShipmentGst1













from .DeliveryAddress import DeliveryAddress



from .ShipmentProduct import ShipmentProduct

from .Store1 import Store1



from .ShipmentDetails1 import ShipmentDetails1











from .Store1 import Store1







from .OrderObj import OrderObj













from .Brand import Brand

from .ShipmentStatusCommon import ShipmentStatusCommon



from .DpDetails1 import DpDetails1

from .Company1 import Company1





from .Bag import Bag



from .ShipmentPrices1 import ShipmentPrices1


class ShipmentDetailsByAffiliateBagIdResponse(BaseSchema):
    # Order swagger.json

    
    einvoice_info = fields.Nested(EinvoiceInfo, required=False)
    
    requested_dp_conf = fields.Nested(RequestedDPConfs, required=False)
    
    payments = fields.Nested(ShipmentPayments, required=False)
    
    shipment_status = fields.Nested(CurrentShipmentStatus, required=False)
    
    total_shipment_bags = fields.Int(required=False)
    
    original_bag_list = fields.List(fields.Int(required=False), required=False)
    
    bag_status_history = fields.List(fields.Nested(BagStatusHistory, required=False), required=False)
    
    user = fields.Nested(UserObj, required=False)
    
    affiliate_details = fields.Nested(AffiliateDetails, required=False)
    
    lock_status = fields.Boolean(required=False)
    
    order_integration_id = fields.Str(required=False)
    
    invoice = fields.Nested(ShipmentInvoice1, required=False)
    
    restore_promos = fields.Dict(required=False)
    
    fallback_user = fields.Dict(required=False)
    
    restore_coupon = fields.Boolean(required=False)
    
    shipment_update_time = fields.Float(required=False)
    
    rto_address = fields.Nested(RtoAddress1, required=False)
    
    shipment_gst = fields.Nested(ShipmentGst1, required=False)
    
    article_details = fields.Dict(required=False)
    
    shipment_value = fields.Float(required=False)
    
    shipment_quantity = fields.Int(required=False)
    
    payment_type = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    delivery_slot = fields.Dict(required=False)
    
    delivery_address = fields.Nested(DeliveryAddress, required=False)
    
    fyndstore_emp = fields.Dict(required=False)
    
    products = fields.List(fields.Nested(ShipmentProduct, required=False), required=False)
    
    ordering_store = fields.Nested(Store1, required=False)
    
    no_of_bags_order = fields.Int(required=False)
    
    shipment = fields.Nested(ShipmentDetails1, required=False)
    
    s_id = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    order_type = fields.Str(required=False)
    
    search_key = fields.Dict(required=False)
    
    comment = fields.Str(required=False)
    
    fulfilling_store = fields.Nested(Store1, required=False)
    
    order_value = fields.Float(required=False)
    
    journey_type = fields.Str(required=False)
    
    payment_methods = fields.Dict(required=False)
    
    order = fields.Nested(OrderObj, required=False)
    
    is_processing = fields.Boolean(required=False)
    
    qc_required = fields.Raw(required=False)
    
    transaction_type = fields.Str(required=False)
    
    total_shipments_in_order = fields.Int(required=False)
    
    cart_id = fields.Int(required=False)
    
    operational_status = fields.Str(required=False)
    
    brand = fields.Nested(Brand, required=False)
    
    shipment_status_history = fields.List(fields.Nested(ShipmentStatusCommon, required=False), required=False)
    
    coupon = fields.Dict(required=False)
    
    dp_details = fields.Nested(DpDetails1, required=False)
    
    company = fields.Nested(Company1, required=False)
    
    order_source = fields.Str(required=False)
    
    weight = fields.Dict(required=False)
    
    bags = fields.List(fields.Nested(Bag, required=False), required=False)
    
    app_id = fields.Str(required=False)
    
    prices = fields.Nested(ShipmentPrices1, required=False)
    

