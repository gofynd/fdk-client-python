"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class DebugInfo(BaseSchema):
    # Orders swagger.json

    
    stormbreaker_uuid = fields.Str(required=False)
    

