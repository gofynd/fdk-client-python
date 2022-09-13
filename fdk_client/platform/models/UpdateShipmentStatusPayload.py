"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .EntitiesDetail import EntitiesDetail




class UpdateShipmentStatusPayload(BaseSchema):
    # Order swagger.json

    
    unlock_before_transition = fields.Boolean(required=False)
    
    process_in_background = fields.Boolean(required=False)
    
    entities = fields.Nested(EntitiesDetail, required=False)
    
    lock_after_transition = fields.Boolean(required=False)
    

