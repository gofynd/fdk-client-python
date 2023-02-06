"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CatalogInsightItem import CatalogInsightItem



from .CatalogInsightBrand import CatalogInsightBrand



class CatalogInsightResponse(BaseSchema):
    #  swagger.json

    
    item = fields.Nested(CatalogInsightItem, required=False)
    
    brand_distribution = fields.Nested(CatalogInsightBrand, required=False)
    
