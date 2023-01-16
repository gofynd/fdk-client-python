"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema


















class DPDetailsData(BaseSchema):
    # Order swagger.json

    
    pincode = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    eway_bill_id = fields.Str(required=False)
    
    track_url = fields.Str(required=False)
    
    gst_tag = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    awb_no = fields.Str(required=False)
    

