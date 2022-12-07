"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema


















class InventoryPayload(BaseSchema):
    #  swagger.json

    
    tags = fields.List(fields.Str(required=False), required=False)
    
    price_effective = fields.Float(required=False)
    
    expiration_date = fields.Str(required=False)
    
    price_marked = fields.Float(required=False)
    
    store_id = fields.Int(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    total_quantity = fields.Int(required=False)
    