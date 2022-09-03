"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class EntityRegionViewRequest(BaseSchema):
    # Serviceability swagger.json

    
    parent_id = fields.List(fields.Str(required=False), required=False)
    
    sub_type = fields.List(fields.Str(required=False), required=False)
    

