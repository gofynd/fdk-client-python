"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class ApplicationItemMOQ(BaseSchema):
    # Catalog swagger.json

    
    multiplier = fields.Int(required=False)
    
    min_qty = fields.Int(required=False)
    
    max_qty = fields.Int(required=False)
    

