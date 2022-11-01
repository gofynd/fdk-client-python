"""User Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class BlockUserRequestSchema(BaseSchema):
    #  swagger.json

    
    status = fields.Boolean(required=False)
    
    user_id = fields.List(fields.Str(required=False), required=False)
    
    reason = fields.Str(required=False)
    
