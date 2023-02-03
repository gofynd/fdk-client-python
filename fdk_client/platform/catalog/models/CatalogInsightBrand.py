"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
















class CatalogInsightBrand(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    available_articles = fields.Int(required=False)
    
    total_articles = fields.Int(required=False)
    
    article_freshness = fields.Int(required=False)
    
    total_sizes = fields.Int(required=False)
    
    available_sizes = fields.Int(required=False)
    
