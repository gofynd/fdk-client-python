"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema















from .InventorySet import InventorySet






















class Size1(BaseSchema):
    # Catalog swagger.json

    
    seller_identifier = fields.Str(required=False)
    
    item_weight_unit_of_measure = fields.Str(required=False)
    
    item_dimensions_unit_of_measure = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    item_height = fields.Float(required=False)
    
    item_width = fields.Float(required=False)
    
    item_weight = fields.Float(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    store_code = fields.Str(required=False)
    
    expiration_date = fields.Str(required=False)
    
    price_effective = fields.Float(required=False)
    
    item_length = fields.Float(required=False)
    
    identifiers = fields.List(fields.Dict(required=False), required=False)
    
    quantity = fields.Int(required=False)
    
    currency = fields.Str(required=False)
    
    price = fields.Float(required=False)
    
    price_transfer = fields.Float(required=False)
    
    is_set = fields.Boolean(required=False)
    
