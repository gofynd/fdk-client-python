"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
























class Dp(BaseSchema):
    #  swagger.json

    
    transport_mode = fields.Str(required=False)
    
    fm_priority = fields.Int(required=False)
    
    area_code = fields.Int(required=False)
    
    external_account_id = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    lm_priority = fields.Int(required=False)
    
    internal_account_id = fields.Str(required=False)
    
    assign_dp_from_sb = fields.Boolean(required=False)
    
    rvp_priority = fields.Int(required=False)
    
    operations = fields.List(fields.Str(required=False), required=False)
    
