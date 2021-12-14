"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class UpdatePasswordRequestSchema(BaseSchema):
    # User swagger.json

    
    old_password = fields.Str(required=False)
    
    new_password = fields.Str(required=False)
    

