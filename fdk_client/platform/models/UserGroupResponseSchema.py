"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






















class UserGroupResponseSchema(BaseSchema):
    # User swagger.json

    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    file_url = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    application_id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    

