"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class EntityRegionView_page(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    item_total = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    

