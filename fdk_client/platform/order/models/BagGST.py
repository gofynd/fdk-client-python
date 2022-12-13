"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




















class BagGST(BaseSchema):
    #  swagger.json

    
    gst_fee = fields.Int(required=False)
    
    brand_calculated_amount = fields.Int(required=False)
    
    hsn_code = fields.Str(required=False)
    
    gstin_code = fields.Str(required=False)
    
    gst_tag = fields.Str(required=False)
    
    value_of_good = fields.Int(required=False)
    
    gst_tax_percentage = fields.Int(required=False)
    
    is_default_hsn_code = fields.Boolean(required=False)
    
