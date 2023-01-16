"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










from .StatuesRequest1 import StatuesRequest1





class UpdateShipmentStatusRequest(BaseSchema):
    #  swagger.json

    
    force_transition = fields.Boolean(required=False)
    
    lock_after_transition = fields.Boolean(required=False)
    
    unlock_before_transition = fields.Boolean(required=False)
    
    statuses = fields.List(fields.Nested(StatuesRequest1, required=False), required=False)
    
    task = fields.Boolean(required=False)
    
