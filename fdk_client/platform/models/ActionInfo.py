"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class ActionInfo(BaseSchema):
    # Order swagger.json

    
    slug = fields.Str(required=False)
    
    display_text = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    id = fields.Int(required=False)
    

