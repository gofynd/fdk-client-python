"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .StatusesBody import StatusesBody











class ShipmentStatusUpdateBody(BaseSchema):
    #  swagger.json

    
    statuses = fields.List(fields.Nested(StatusesBody, required=False), required=False)
    
    unlock_before_transition = fields.Boolean(required=False)
    
    task = fields.Boolean(required=False)
    
    force_transition = fields.Boolean(required=False)
    
    lock_after_transition = fields.Boolean(required=False)
    
