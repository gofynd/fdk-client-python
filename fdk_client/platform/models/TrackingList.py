"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class TrackingList(BaseSchema):
    # Orders swagger.json

    
    time = fields.Str(required=False)
    
    is_passed = fields.Boolean(required=False)
    
    status = fields.Str(required=False)
    
    is_current = fields.Boolean(required=False)
    

