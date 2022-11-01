"""Payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class WalletOtpResponse(BaseSchema):
    #  swagger.json

    
    request_id = fields.Str(required=False)
    
    is_verified_flag = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
