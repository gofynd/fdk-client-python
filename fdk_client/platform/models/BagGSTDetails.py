"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema


































class BagGSTDetails(BaseSchema):
    # Order swagger.json

    
    gst_fee = fields.Float(required=False)
    
    tax_collected_at_source = fields.Float(required=False)
    
    hsn_code_id = fields.Str(required=False)
    
    cgst_gst_fee = fields.Str(required=False)
    
    igst_tax_percentage = fields.Float(required=False)
    
    value_of_good = fields.Float(required=False)
    
    igst_gst_fee = fields.Str(required=False)
    
    hsn_code = fields.Str(required=False)
    
    brand_calculated_amount = fields.Float(required=False)
    
    cgst_tax_percentage = fields.Float(required=False)
    
    sgst_gst_fee = fields.Str(required=False)
    
    gst_tag = fields.Str(required=False)
    
    sgst_tax_percentage = fields.Float(required=False)
    
    is_default_hsn_code = fields.Boolean(required=False)
    
    gstin_code = fields.Str(required=False)
    
    gst_tax_percentage = fields.Float(required=False)
    

