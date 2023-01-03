"""payment Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class UpdatePayoutRequest(BaseSchema):
    #  swagger.json

    
    unique_external_id = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
