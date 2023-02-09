"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema


















class BagGST(BaseSchema):
    # Orders swagger.json

    
    gstin_code = fields.Str(required=False)
    
    gst_tag = fields.Str(required=False)
    
    gst_fee = fields.Int(required=False)
    
    gst_tax_percentage = fields.Int(required=False)
    
    hsn_code = fields.Str(required=False)
    
    value_of_good = fields.Int(required=False)
    
    is_default_hsn_code = fields.Boolean(required=False)
    
    brand_calculated_amount = fields.Int(required=False)
    

