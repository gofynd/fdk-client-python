"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
















class BulkInventoryPayload(BaseSchema):
    # Catalog swagger.json

    
    item_id = fields.Int(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    expiration_date = fields.Str(required=False)
    
    price_effective = fields.Float(required=False)
    
    price_marked = fields.Float(required=False)
    
    total_quantity = fields.Int(required=False)
    
    store_id = fields.Int(required=False)
    

