"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class BulkListingPage(BaseSchema):
    # Orders swagger.json

    
    has_next = fields.Boolean(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    current = fields.Int(required=False)
    
    total = fields.Int(required=False)
    
