"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




















class DPDetailsData(BaseSchema):
    #  swagger.json

    
    track_url = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    country = fields.Str(required=False)
    
    awb_no = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    eway_bill_id = fields.Str(required=False)
    
    gst_tag = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
