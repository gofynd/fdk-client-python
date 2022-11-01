"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CatalogInsightBrand import CatalogInsightBrand



from .CatalogInsightItem import CatalogInsightItem



class CatalogInsightResponse(BaseSchema):
    #  swagger.json

    
    brand_distribution = fields.Nested(CatalogInsightBrand, required=False)
    
    item = fields.Nested(CatalogInsightItem, required=False)
    
