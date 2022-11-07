"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema


























class InventoryJobPayload(BaseSchema):
    # Catalog swagger.json

    
    price = fields.Float(required=False)
    
    expiration_date = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    price_effective = fields.Float(required=False)
    
    price_marked = fields.Float(required=False)
    
    total_quantity = fields.Int(required=False)
    
    store_code = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    item_weight_unit_of_measure = fields.Str(required=False)
    
    item_dimensions_unit_of_measure = fields.Str(required=False)
    

