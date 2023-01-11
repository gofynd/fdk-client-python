"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .EntityReasonData import EntityReasonData




class EntitiesReasons(BaseSchema):
    # Order swagger.json

    
    data = fields.Nested(EntityReasonData, required=False)
    
    filters = fields.List(fields.Dict(required=False), required=False)
    

