"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CatalogInsightBrand import CatalogInsightBrand



from .CrossSellingData import CrossSellingData



class CrossSellingResponse(BaseSchema):
    #  swagger.json

    
    brand_distribution = fields.Nested(CatalogInsightBrand, required=False)
    
    data = fields.Nested(CrossSellingData, required=False)
    
