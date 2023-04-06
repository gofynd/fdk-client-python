"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema


















class BagGST(BaseSchema):
    # Order swagger.json

    
    is_default_hsn_code = fields.Boolean(required=False)
    
    value_of_good = fields.Float(required=False)
    
    gst_fee = fields.Float(required=False)
    
    gst_tax_percentage = fields.Int(required=False)
    
    brand_calculated_amount = fields.Float(required=False)
    
    hsn_code = fields.Str(required=False)
    
    gst_tag = fields.Str(required=False)
    
    gstin_code = fields.Str(required=False)
    

