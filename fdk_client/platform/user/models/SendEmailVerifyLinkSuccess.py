"""user Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class SendEmailVerifyLinkSuccess(BaseSchema):
    #  swagger.json

    
    verify_email_link = fields.Boolean(required=False)
    
