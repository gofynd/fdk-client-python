"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class ApplicationItemMOQ(BaseSchema):
    # Catalog swagger.json

    
    minimum = fields.Int(required=False)
    
    increment_unit = fields.Int(required=False)
    
    maximum = fields.Int(required=False)
    
