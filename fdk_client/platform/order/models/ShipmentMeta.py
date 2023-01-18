"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












from .Formatted import Formatted





from .LockData import LockData





from .ShipmentTimeStamp import ShipmentTimeStamp











from .EinvoiceInfo import EinvoiceInfo









from .BuyerDetails import BuyerDetails









from .DebugInfo import DebugInfo































class ShipmentMeta(BaseSchema):
    #  swagger.json

    
    assign_dp_from_sb = fields.Boolean(required=False)
    
    external = fields.Dict(required=False)
    
    packaging_name = fields.Str(required=False)
    
    forward_affiliate_order_id = fields.Str(required=False)
    
    formatted = fields.Nested(Formatted, required=False)
    
    ewaybill_info = fields.Dict(required=False)
    
    lock_data = fields.Nested(LockData, required=False)
    
    dp_name = fields.Str(required=False)
    
    timestamp = fields.Nested(ShipmentTimeStamp, required=False)
    
    due_date = fields.Str(required=False)
    
    weight = fields.Int(required=False)
    
    return_store_node = fields.Int(required=False)
    
    auto_trigger_dp_assignment_acf = fields.Boolean(required=False)
    
    einvoice_info = fields.Nested(EinvoiceInfo, required=False)
    
    dp_options = fields.Dict(required=False)
    
    return_affiliate_shipment_id = fields.Str(required=False)
    
    po_number = fields.Str(required=False)
    
    b2b_buyer_details = fields.Nested(BuyerDetails, required=False)
    
    dp_sort_key = fields.Str(required=False)
    
    b2c_buyer_details = fields.Dict(required=False)
    
    fulfilment_priority_text = fields.Str(required=False)
    
    debug_info = fields.Nested(DebugInfo, required=False)
    
    dp_id = fields.Str(required=False)
    
    return_awb_number = fields.Str(required=False)
    
    order_type = fields.Str(required=False)
    
    marketplace_store_id = fields.Str(required=False)
    
    same_store_available = fields.Boolean(required=False)
    
    awb_number = fields.Str(required=False)
    
    box_type = fields.Str(required=False)
    
    shipment_weight = fields.Float(required=False)
    
    forward_affiliate_shipment_id = fields.Str(required=False)
    
    return_details = fields.Dict(required=False)
    
    shipment_volumetric_weight = fields.Float(required=False)
    
    bag_weight = fields.Dict(required=False)
    
    return_affiliate_order_id = fields.Str(required=False)
    
    store_invoice_updated_date = fields.Str(required=False)
    
