"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




















class OmsReports(BaseSchema):
    # Order swagger.json

    
    report_type = fields.Str(required=False)
    
    report_requested_at = fields.Str(required=False)
    
    s3_key = fields.Str(required=False)
    
    request_details = fields.Dict(required=False)
    
    display_name = fields.Str(required=False)
    
    report_id = fields.Str(required=False)
    
    report_name = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    report_created_at = fields.Str(required=False)
    

