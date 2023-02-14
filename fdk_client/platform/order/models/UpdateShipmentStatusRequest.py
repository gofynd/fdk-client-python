"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .StatuesRequest import StatuesRequest





class UpdateShipmentStatusRequest(BaseSchema):
    #  swagger.json

    
    lock_after_transition = fields.Boolean(required=False)
    
    force_transition = fields.Boolean(required=False)
    
    task = fields.Boolean(required=False)
    
    statuses = fields.List(fields.Nested(StatuesRequest, required=False), required=False)
    
    unlock_before_transition = fields.Boolean(required=False)
    
