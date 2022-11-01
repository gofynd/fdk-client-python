"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class SessionExpiry(BaseSchema):
    # User swagger.json

    
    duration = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    

