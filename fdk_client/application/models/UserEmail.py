"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class UserEmail(BaseSchema):
    # User swagger.json

    
    primary = fields.Boolean(required=False)
    
    verified = fields.Boolean(required=False)
    
    email = fields.Str(required=False)
    
    active = fields.Boolean(required=False)
    

