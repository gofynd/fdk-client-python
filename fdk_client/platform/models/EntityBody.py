"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .DataUpdate import DataUpdate







from .EntityReason import EntityReason


class EntityBody(BaseSchema):
    # Order swagger.json

    
    data_updates = fields.Nested(DataUpdate, required=False)
    
    next_status = fields.Str(required=False)
    
    entity_ids = fields.List(fields.Str(required=False), required=False)
    
    bag_ids = fields.List(fields.Str(required=False), required=False)
    
    reasons = fields.Nested(EntityReason, required=False)
    

