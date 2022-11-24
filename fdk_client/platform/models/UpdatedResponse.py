"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class UpdatedResponse(BaseSchema):
    # Catalog swagger.json

    
    items_not_updated = fields.List(fields.Int(required=False), required=False)
    
    message = fields.Str(required=False)
    

