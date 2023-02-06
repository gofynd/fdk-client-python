"""communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class VerifyOtpCommsSuccessRes(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    
    mobile = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
