"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class BillingStaffDetails(BaseSchema):
    # Order swagger.json

    
    employee_code = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    staff_id = fields.Int(required=False)
    
    user = fields.Str(required=False)
    

