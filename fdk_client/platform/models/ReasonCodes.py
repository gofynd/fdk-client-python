"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class ReasonCodes(BaseSchema):
    # Order swagger.json

    
    category = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    id = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    
    state = fields.Str(required=False)
    

