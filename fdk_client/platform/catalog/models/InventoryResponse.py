"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






























class InventoryResponse(BaseSchema):
    #  swagger.json

    
    price_transfer = fields.Float(required=False)
    
    size = fields.Str(required=False)
    
    price = fields.Float(required=False)
    
    price_effective = fields.Float(required=False)
    
    inventory_updated_on = fields.Str(required=False)
    
    sellable_quantity = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    
    store = fields.Dict(required=False)
    
    identifiers = fields.Dict(required=False)
    
    item_id = fields.Int(required=False)
    
    uid = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    