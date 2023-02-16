"""user Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class SendEmailVerifyLinkSuccess(BaseSchema):
    #  swagger.json

    
    verify_email_link = fields.Boolean(required=False)
    
