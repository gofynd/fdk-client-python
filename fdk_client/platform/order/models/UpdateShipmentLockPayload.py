"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Entities import Entities









class UpdateShipmentLockPayload(BaseSchema):
    #  swagger.json

    
    entities = fields.List(fields.Nested(Entities, required=False), required=False)
    
    action_type = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
