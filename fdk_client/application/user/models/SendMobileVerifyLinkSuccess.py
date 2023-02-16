"""user Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class SendMobileVerifyLinkSuccess(BaseSchema):
    #  swagger.json

    
    verify_mobile_link = fields.Boolean(required=False)
    
