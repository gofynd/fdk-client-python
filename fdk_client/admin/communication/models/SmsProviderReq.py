"""communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema


















class SmsProviderReq(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    sender = fields.Str(required=False)
    
    username = fields.Str(required=False)
    
    authkey = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    provider = fields.Str(required=False)
    
