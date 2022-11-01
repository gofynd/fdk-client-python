"""Payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class RefundAccountResponse(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    
    is_verified_flag = fields.Boolean(required=False)
    
    success = fields.Boolean(required=False)
    
