"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class CatalogInsightItem(BaseSchema):
    #  swagger.json

    
    count = fields.Int(required=False)
    
    out_of_stock_count = fields.Int(required=False)
    
    sellable_count = fields.Int(required=False)
    
