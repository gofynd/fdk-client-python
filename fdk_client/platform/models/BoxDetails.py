"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class BoxDetails(BaseSchema):
    # DocumentEngine swagger.json

    
    box_id = fields.Str(required=False)
    
    total_quantity = fields.Str(required=False)
    
    package_count = fields.Str(required=False)
    
    dimension = fields.Str(required=False)
    
    weight = fields.Str(required=False)
    

