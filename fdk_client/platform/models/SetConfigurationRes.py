"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class SetConfigurationRes(BaseSchema):
    # Rewards swagger.json

    
    success = fields.Boolean(required=False)
    

