"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class Size(BaseSchema):
    # Catalog swagger.json

    
    value = fields.Raw(required=False)
    
    display = fields.Raw(required=False)
    
    quantity = fields.Int(required=False)
    
    is_available = fields.Boolean(required=False)
    

