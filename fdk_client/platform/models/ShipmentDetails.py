"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

















from .ShippingToAddress import ShippingToAddress

from .SellerAddress import SellerAddress


class ShipmentDetails(BaseSchema):
    # DocumentEngine swagger.json

    
    shipment_no = fields.Str(required=False)
    
    appointment_no = fields.Str(required=False)
    
    total_sku = fields.Str(required=False)
    
    item_qty = fields.Str(required=False)
    
    no_of_boxes = fields.Str(required=False)
    
    shipping_to = fields.Str(required=False)
    
    seller_name = fields.Str(required=False)
    
    gstin_number = fields.Str(required=False)
    
    shipping_address = fields.Nested(ShippingToAddress, required=False)
    
    seller_address = fields.Nested(SellerAddress, required=False)
    

