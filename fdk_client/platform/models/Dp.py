"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






















class Dp(BaseSchema):
    # Serviceability swagger.json

    
    payment_mode = fields.Str(required=False)
    
    operations = fields.List(fields.Str(required=False), required=False)
    
    external_account_id = fields.Str(required=False)
    
    assign_dp_from_sb = fields.Boolean(required=False)
    
    area_code = fields.Int(required=False)
    
    transport_mode = fields.Str(required=False)
    
    lm_priority = fields.Int(required=False)
    
    internal_account_id = fields.Str(required=False)
    
    rvp_priority = fields.Int(required=False)
    
    fm_priority = fields.Int(required=False)
    

