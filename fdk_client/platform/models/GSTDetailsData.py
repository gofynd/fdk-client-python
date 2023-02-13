"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class GSTDetailsData(BaseSchema):
    # Orders swagger.json

    
    tax_collected_at_source = fields.Float(required=False)
    
    value_of_good = fields.Float(required=False)
    
    gstin_code = fields.Str(required=False)
    
    gst_fee = fields.Float(required=False)
    
    brand_calculated_amount = fields.Float(required=False)
    

