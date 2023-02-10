"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class SendOtpToCustomerResponse(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
    resend_timer = fields.Int(required=False)
    
    request_id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
