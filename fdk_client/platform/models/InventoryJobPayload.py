"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class InventoryJobPayload(BaseSchema):
    # Catalog swagger.json

    
    total_quantity = fields.Int(required=False)
    
    price_marked = fields.Float(required=False)
    
    price_effective = fields.Float(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    store_code = fields.Str(required=False)
    
    expiration_date = fields.Str(required=False)
    
