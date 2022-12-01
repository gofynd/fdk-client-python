"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ProductCompareResponse import ProductCompareResponse



class ProductFrequentlyComparedSimilarResponse(BaseSchema):
    #  swagger.json

    
    similars = fields.Nested(ProductCompareResponse, required=False)
    
