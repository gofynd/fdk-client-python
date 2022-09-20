"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class RecursiveUpdate(BaseSchema):
    # Order swagger.json

    
    bag_ids = fields.List(fields.Str(required=False), required=False)
    
    entity_ids = fields.List(fields.Str(required=False), required=False)
    

