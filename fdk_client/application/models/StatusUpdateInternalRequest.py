"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .StatuesRequest import StatuesRequest








class StatusUpdateInternalRequest(BaseSchema):
    # Order swagger.json

    
    force_transition = fields.Boolean(required=False)
    
    statues = fields.List(fields.Nested(StatuesRequest, required=False), required=False)
    
    task = fields.Boolean(required=False)
    
    unlock_before_transition = fields.Boolean(required=False)
    
    lock_after_transition = fields.Boolean(required=False)
    

