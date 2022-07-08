"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class InventoryJobPayload(BaseSchema):
    # Catalog swagger.json

    
    price_effective = fields.Float(required=False)
    
    store_code = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    expiration_date = fields.Str(required=False)
    
    price = fields.Float(required=False)
    
    seller_identifier = fields.Str(required=False)
    

