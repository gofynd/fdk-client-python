"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CrossSellingData import CrossSellingData



from .CatalogInsightBrand import CatalogInsightBrand



class CrossSellingResponse(BaseSchema):
    #  swagger.json

    
    data = fields.Nested(CrossSellingData, required=False)
    
    brand_distribution = fields.Nested(CatalogInsightBrand, required=False)
    
