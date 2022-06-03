"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






















class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    total_quantity = fields.Int(required=False)
    
    identifier = fields.Dict(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    store = fields.Dict(required=False)
    
    sellable = fields.Dict(required=False)
    
    uid = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    price = fields.Dict(required=False)
    
    inventory_updated_on = fields.Str(required=False)
    

