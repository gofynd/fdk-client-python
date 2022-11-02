"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






























class InventoryResponse(BaseSchema):
    #  swagger.json

    
    store = fields.Dict(required=False)
    
    currency = fields.Str(required=False)
    
    identifiers = fields.Dict(required=False)
    
    quantity = fields.Int(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    price_effective = fields.Float(required=False)
    
    uid = fields.Str(required=False)
    
    sellable_quantity = fields.Int(required=False)
    
    price = fields.Float(required=False)
    
    price_transfer = fields.Float(required=False)
    
    item_id = fields.Int(required=False)
    
    inventory_updated_on = fields.Str(required=False)
    
