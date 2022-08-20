"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .DataUpdate import DataUpdate

from .EntityReason import EntityReason


class EntityBody(BaseSchema):
    # Order swagger.json

    
    bag_ids = fields.List(fields.Str(required=False), required=False)
    
    entity_ids = fields.List(fields.Str(required=False), required=False)
    
    next_status = fields.Str(required=False)
    
    data_updates = fields.Nested(DataUpdate, required=False)
    
    reasons = fields.Nested(EntityReason, required=False)
    

