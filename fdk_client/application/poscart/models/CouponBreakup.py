"""poscart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema
















class CouponBreakup(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    is_applied = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    value = fields.Float(required=False)
    
