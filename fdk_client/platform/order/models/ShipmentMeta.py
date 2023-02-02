"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




























from .Formatted import Formatted



from .EinvoiceInfo import EinvoiceInfo















from .LockData import LockData















from .DebugInfo import DebugInfo











from .BuyerDetails import BuyerDetails







from .ShipmentTimeStamp import ShipmentTimeStamp



class ShipmentMeta(BaseSchema):
    #  swagger.json

    
    dp_options = fields.Dict(required=False)
    
    shipment_weight = fields.Float(required=False)
    
    dp_sort_key = fields.Str(required=False)
    
    b2c_buyer_details = fields.Dict(required=False)
    
    ewaybill_info = fields.Dict(required=False)
    
    dp_name = fields.Str(required=False)
    
    auto_trigger_dp_assignment_acf = fields.Boolean(required=False)
    
    return_store_node = fields.Int(required=False)
    
    forward_affiliate_shipment_id = fields.Str(required=False)
    
    awb_number = fields.Str(required=False)
    
    due_date = fields.Str(required=False)
    
    bag_weight = fields.Dict(required=False)
    
    formatted = fields.Nested(Formatted, required=False)
    
    einvoice_info = fields.Nested(EinvoiceInfo, required=False)
    
    assign_dp_from_sb = fields.Boolean(required=False)
    
    store_invoice_updated_date = fields.Str(required=False)
    
    return_details = fields.Dict(required=False)
    
    return_affiliate_order_id = fields.Str(required=False)
    
    shipment_volumetric_weight = fields.Float(required=False)
    
    po_number = fields.Str(required=False)
    
    lock_data = fields.Nested(LockData, required=False)
    
    order_type = fields.Str(required=False)
    
    return_affiliate_shipment_id = fields.Str(required=False)
    
    weight = fields.Int(required=False)
    
    external = fields.Dict(required=False)
    
    fulfilment_priority_text = fields.Str(required=False)
    
    dp_id = fields.Str(required=False)
    
    debug_info = fields.Nested(DebugInfo, required=False)
    
    packaging_name = fields.Str(required=False)
    
    marketplace_store_id = fields.Str(required=False)
    
    return_awb_number = fields.Str(required=False)
    
    same_store_available = fields.Boolean(required=False)
    
    b2b_buyer_details = fields.Nested(BuyerDetails, required=False)
    
    box_type = fields.Str(required=False)
    
    forward_affiliate_order_id = fields.Str(required=False)
    
    timestamp = fields.Nested(ShipmentTimeStamp, required=False)
    
