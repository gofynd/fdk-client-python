"""AuditTrail Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class EntityObject(BaseSchema):
    #  swagger.json

    
    id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
