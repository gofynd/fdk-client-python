"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class UpdateUserGroupSchema(BaseSchema):
    # User swagger.json

    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    file_url = fields.Str(required=False)
    

