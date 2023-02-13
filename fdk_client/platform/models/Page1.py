"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class Page1(BaseSchema):
    # Orders swagger.json

    
    has_next = fields.Boolean(required=False)
    
    item_total = fields.Int(required=False)
    
    page_type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    current = fields.Int(required=False)
    

