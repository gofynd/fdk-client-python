"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .InventoryJobPayload import InventoryJobPayload




class InventoryBulkRequest(BaseSchema):
    # Catalog swagger.json

    
    user = fields.Dict(required=False)
    
    company_id = fields.Int(required=False)
    
    sizes = fields.List(fields.Nested(InventoryJobPayload, required=False), required=False)
    
    batch_id = fields.Str(required=False)
    

