"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema















from .ShippingAddress import ShippingAddress

from .SellerAddress import SellerAddress


class ShipmentDetails(BaseSchema):
    # OrderInvoiceEngine swagger.json

    
    shipment_no = fields.Str(required=False)
    
    appointment_no = fields.Str(required=False)
    
    total_sku = fields.Str(required=False)
    
    item_qty = fields.Str(required=False)
    
    no_of_boxes = fields.Str(required=False)
    
    shipping_to = fields.Str(required=False)
    
    gstin_number = fields.Str(required=False)
    
    shipping_address = fields.Nested(ShippingAddress, required=False)
    
    seller_address = fields.Nested(SellerAddress, required=False)
    

