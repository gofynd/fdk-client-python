"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema
















class CouponBreakup(BaseSchema):
    #  swagger.json

    
    value = fields.Float(required=False)
    
    code = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    is_applied = fields.Boolean(required=False)
    
