"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class CouponAction(BaseSchema):
    #  swagger.json

    
    action_date = fields.Str(required=False)
    
    txn_mode = fields.Str(required=False)
    
