"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class BagStatusHistory(BaseSchema):
    # Order swagger.json

    
    status = fields.Str(required=False)
    
    display_name = fields.Boolean(required=False)
    
    updated_at = fields.Str(required=False)
    
    app_display_name = fields.Boolean(required=False)
    
    forward = fields.Boolean(required=False)
    
    state_type = fields.Boolean(required=False)
    

