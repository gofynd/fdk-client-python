"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class ResendPaymentLinkResponse(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    
    status_code = fields.Int(required=False)
    
    polling_timeout = fields.Int(required=False)
    
    message = fields.Str(required=False)
    