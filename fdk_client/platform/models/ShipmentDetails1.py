"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ShipmentHandOverCustomerContact import ShipmentHandOverCustomerContact



















from .PDFLinks import PDFLinks



from .DeliveryAddress import DeliveryAddress







from .ShipmentMeta import ShipmentMeta







from .BillingAddress1 import BillingAddress1




class ShipmentDetails1(BaseSchema):
    # Order swagger.json

    
    created_at = fields.Int(required=False)
    
    hand_over_contact_json = fields.Nested(ShipmentHandOverCustomerContact, required=False)
    
    parent_id = fields.Str(required=False)
    
    affiliate_id = fields.Str(required=False)
    
    lock_status = fields.Str(required=False)
    
    packaging_type = fields.Str(required=False)
    
    eway_bill_id = fields.Str(required=False)
    
    affiliate_shipment_id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    s_id = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    pdf_links = fields.Nested(PDFLinks, required=False)
    
    fulfilment_priority = fields.Int(required=False)
    
    delivery_address_json = fields.Nested(DeliveryAddress, required=False)
    
    parent_type = fields.Str(required=False)
    
    previous_shipment_id = fields.Str(required=False)
    
    sd_type = fields.Str(required=False)
    
    meta = fields.Nested(ShipmentMeta, required=False)
    
    store_invoice_id = fields.Str(required=False)
    
    credit_note_id = fields.Str(required=False)
    
    fynd_order_id = fields.Str(required=False)
    
    billing_address_json = fields.Nested(BillingAddress1, required=False)
    
    delivery_awb_number = fields.Str(required=False)
    

