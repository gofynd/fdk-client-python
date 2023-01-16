"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class BulkListingPage(BaseSchema):
    # Order swagger.json

    
    has_previous = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    total = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    type = fields.Str(required=False)
    

