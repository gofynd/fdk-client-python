"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class UnauthenticatedUser(BaseSchema):
    # Billing swagger.json

    
    message = fields.Str(required=False)
    
