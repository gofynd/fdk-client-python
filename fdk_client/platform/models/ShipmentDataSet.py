"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema























from .ShipmentPricesDataInfo import ShipmentPricesDataInfo










class ShipmentDataSet(BaseSchema):
    # Orders swagger.json

    
    cashback = fields.Int(required=False)
    
    value_of_good = fields.Int(required=False)
    
    shipment_id = fields.Str(required=False)
    
    shipment_images = fields.List(fields.Str(required=False), required=False)
    
    refund_credit = fields.Int(required=False)
    
    brand_calculated_amount = fields.Int(required=False)
    
    total_bags = fields.Int(required=False)
    
    fynd_credits = fields.Int(required=False)
    
    cashback_applied = fields.Int(required=False)
    
    tax_collected_at_source = fields.Int(required=False)
    
    total_items = fields.Int(required=False)
    
    prices = fields.Nested(ShipmentPricesDataInfo, required=False)
    
    shipment_status = fields.Dict(required=False)
    
    delivery_charge = fields.Int(required=False)
    
    coupon_effective_discount = fields.Int(required=False)
    
    price_effective = fields.Int(required=False)
    

