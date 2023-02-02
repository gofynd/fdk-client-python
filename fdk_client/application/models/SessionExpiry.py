"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class SessionExpiry(BaseSchema):
    # User swagger.json

    
    duration = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    is_rolling = fields.Boolean(required=False)
    

