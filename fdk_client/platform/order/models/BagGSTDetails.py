"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




































class BagGSTDetails(BaseSchema):
    #  swagger.json

    
    cgst_tax_percentage = fields.Float(required=False)
    
    sgst_gst_fee = fields.Str(required=False)
    
    gst_tag = fields.Str(required=False)
    
    igst_gst_fee = fields.Str(required=False)
    
    hsn_code_id = fields.Str(required=False)
    
    is_default_hsn_code = fields.Boolean(required=False)
    
    cgst_gst_fee = fields.Str(required=False)
    
    gstin_code = fields.Str(required=False)
    
    brand_calculated_amount = fields.Float(required=False)
    
    tax_collected_at_source = fields.Float(required=False)
    
    igst_tax_percentage = fields.Float(required=False)
    
    gst_tax_percentage = fields.Float(required=False)
    
    sgst_tax_percentage = fields.Float(required=False)
    
    hsn_code = fields.Str(required=False)
    
    gst_fee = fields.Float(required=False)
    
    value_of_good = fields.Float(required=False)
    
