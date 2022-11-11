"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




























class InventoryJobPayload(BaseSchema):
    #  swagger.json

    
    price_marked = fields.Float(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    item_dimensions_unit_of_measure = fields.Str(required=False)
    
    store_code = fields.Str(required=False)
    
    expiration_date = fields.Str(required=False)
    
    price = fields.Float(required=False)
    
    item_weight_unit_of_measure = fields.Str(required=False)
    
    price_effective = fields.Float(required=False)
    
    currency = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    total_quantity = fields.Int(required=False)
    
