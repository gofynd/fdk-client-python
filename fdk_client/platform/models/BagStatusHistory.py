"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class BagStatusHistory(BaseSchema):
    # Orders swagger.json

    
    app_display_name = fields.Boolean(required=False)
    
    state_type = fields.Boolean(required=False)
    
    display_name = fields.Boolean(required=False)
    
    forward = fields.Boolean(required=False)
    
    updated_at = fields.Str(required=False)
    
    status = fields.Str(required=False)
    

