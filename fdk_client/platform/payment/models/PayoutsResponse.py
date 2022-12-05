"""payment Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema


















class PayoutsResponse(BaseSchema):
    #  swagger.json

    
    is_default = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    transfer_type = fields.Str(required=False)
    
    customers = fields.Dict(required=False)
    
    more_attributes = fields.Dict(required=False)
    
    payouts_aggregators = fields.List(fields.Dict(required=False), required=False)
    
    unique_transfer_no = fields.Dict(required=False)
    
