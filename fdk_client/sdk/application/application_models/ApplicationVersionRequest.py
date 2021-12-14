"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema












class ApplicationVersionRequest(BaseSchema):
    # Configuration swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    namespace = fields.Str(required=False)
    
    token = fields.Str(required=False)
    
    version = fields.Str(required=False)
    

