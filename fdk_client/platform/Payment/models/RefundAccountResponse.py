"""Payment Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class RefundAccountResponse(BaseSchema):
    #  swagger.json

    
    is_verified_flag = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    data = fields.Dict(required=False)
    
