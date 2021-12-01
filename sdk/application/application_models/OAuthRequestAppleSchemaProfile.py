"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema








class OAuthRequestAppleSchemaProfile(BaseSchema):

    
    last_name = fields.Str(required=False)
    
    full_name = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    

