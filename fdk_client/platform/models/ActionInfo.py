"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class ActionInfo(BaseSchema):
    # Order swagger.json

    
    description = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    display_text = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    

