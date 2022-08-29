"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .InventoryError import InventoryError


class InventoryFailedReason(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    
    errors = fields.List(fields.Nested(InventoryError, required=False), required=False)
    

