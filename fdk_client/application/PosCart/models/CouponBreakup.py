"""PosCart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema
















class CouponBreakup(BaseSchema):
    #  swagger.json

    
    code = fields.Str(required=False)
    
    value = fields.Float(required=False)
    
    uid = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    is_applied = fields.Boolean(required=False)
    
