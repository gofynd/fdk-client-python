"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
















class CatalogInsightBrand(BaseSchema):
    #  swagger.json

    
    article_freshness = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    total_sizes = fields.Int(required=False)
    
    available_articles = fields.Int(required=False)
    
    total_articles = fields.Int(required=False)
    
    available_sizes = fields.Int(required=False)
    
