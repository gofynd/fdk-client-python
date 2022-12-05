"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class SendOtpToCustomerResponse(BaseSchema):
    #  swagger.json

    
    resend_timer = fields.Int(required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    request_id = fields.Str(required=False)
    
