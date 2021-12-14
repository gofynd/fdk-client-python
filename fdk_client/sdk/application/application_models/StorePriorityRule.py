"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class StorePriorityRule(BaseSchema):
    # Configuration swagger.json

    
    enabled = fields.Boolean(required=False)
    
    storetype_order = fields.List(fields.Str(required=False), required=False)
    

