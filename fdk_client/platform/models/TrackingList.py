"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class TrackingList(BaseSchema):
    # Order swagger.json

    
    is_passed = fields.Boolean(required=False)
    
    time = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    text = fields.Str(required=False)
    
    is_current = fields.Boolean(required=False)
    

