"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .SmsDataPayload import SmsDataPayload




class SendSmsPayload(BaseSchema):
    # OrderManage swagger.json

    
    bag_id = fields.Int(required=False)
    
    data = fields.Nested(SmsDataPayload, required=False)
    
    slug = fields.Str(required=False)
    

