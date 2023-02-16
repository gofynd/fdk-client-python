"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .SmsDataPayload import SmsDataPayload







class SendSmsPayload(BaseSchema):
    #  swagger.json

    
    data = fields.Nested(SmsDataPayload, required=False)
    
    slug = fields.Str(required=False)
    
    bag_id = fields.Int(required=False)
    
