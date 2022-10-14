"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class BagStatusHistory(BaseSchema):
    # Orders swagger.json

    
    updated_at = fields.Str(required=False)
    
    forward = fields.Boolean(required=False)
    
    status = fields.Str(required=False)
    
    display_name = fields.Boolean(required=False)
    
    app_display_name = fields.Boolean(required=False)
    
    state_type = fields.Boolean(required=False)
    

