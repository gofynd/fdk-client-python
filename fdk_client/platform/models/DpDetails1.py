"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




















class DpDetails1(BaseSchema):
    # Order swagger.json

    
    awb_no = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    dp_charges = fields.Int(required=False)
    
    amount_handling_charges = fields.Int(required=False)
    
    dp_return_charges = fields.Int(required=False)
    
    gst_tag = fields.Str(required=False)
    
    eway_bill_id = fields.Str(required=False)
    
    track_url = fields.Str(required=False)
    
    dpd_id = fields.Str(required=False)
    

