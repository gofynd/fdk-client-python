"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class ConfigurationRes(BaseSchema):
    # Rewards swagger.json

    
    valid_android_packages = fields.List(fields.Str(required=False), required=False)
    
    terms_conditions_link = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    

