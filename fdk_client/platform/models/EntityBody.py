"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .EntityReason import EntityReason



from .DataUpdate import DataUpdate




class EntityBody(BaseSchema):
    # Order swagger.json

    
    next_status = fields.Str(required=False)
    
    reasons = fields.Nested(EntityReason, required=False)
    
    bag_ids = fields.List(fields.Str(required=False), required=False)
    
    data_updates = fields.Nested(DataUpdate, required=False)
    
    entity_ids = fields.List(fields.Str(required=False), required=False)
    

