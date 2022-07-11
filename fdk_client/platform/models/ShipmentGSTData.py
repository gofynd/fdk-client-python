"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class ShipmentGSTData(BaseSchema):
    # Orders swagger.json

    
    gstin_code = fields.Str(required=False)
    
    tax_collected_at_source = fields.Int(required=False)
    
    gst_fee = fields.Int(required=False)
    
    value_of_good = fields.Int(required=False)
    
    brand_calculated_amount = fields.Int(required=False)
    

