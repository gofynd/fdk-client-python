"""payment Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class WrongOtpError(BaseSchema):
    #  swagger.json

    
    description = fields.Str(required=False)
    
    is_verified_flag = fields.Boolean(required=False)
    
    success = fields.Str(required=False)
    
