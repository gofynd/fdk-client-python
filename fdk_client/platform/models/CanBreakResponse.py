"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class CanBreakResponse(BaseSchema):
    # Order swagger.json

    
    status = fields.Boolean(required=False)
    
    valid_actions = fields.Dict(required=False)
    

