"""Payment Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class UpdatePayoutResponse(BaseSchema):
    #  swagger.json

    
    is_active = fields.Boolean(required=False)
    
    success = fields.Boolean(required=False)
    
    is_default = fields.Boolean(required=False)
    
