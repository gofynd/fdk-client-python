"""Communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class SmsTemplateMessage(BaseSchema):
    #  swagger.json

    
    template_type = fields.Str(required=False)
    
    template = fields.Str(required=False)
    
