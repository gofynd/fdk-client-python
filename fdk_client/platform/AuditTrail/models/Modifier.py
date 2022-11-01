"""AuditTrail Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class Modifier(BaseSchema):
    #  swagger.json

    
    user_id = fields.Str(required=False)
    
    as_administrator = fields.Boolean(required=False)
    
    user_details = fields.Dict(required=False)
    
