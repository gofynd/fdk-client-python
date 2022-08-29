"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class InventoryError(BaseSchema):
    # Catalog swagger.json

    
    error = fields.Str(required=False)
    
    key = fields.Str(required=False)
    

