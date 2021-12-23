"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema




























class InventoryResponse(BaseSchema):
    # Catalog swagger.json

    
    sellable_quantity = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    
    store = fields.Dict(required=False)
    
    seller_identifier = fields.Int(required=False)
    
    inventory_updated_on = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    identifiers = fields.Dict(required=False)
    
    price_effective = fields.Int(required=False)
    
    price = fields.Int(required=False)
    
    uid = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    price_transfer = fields.Int(required=False)
    

