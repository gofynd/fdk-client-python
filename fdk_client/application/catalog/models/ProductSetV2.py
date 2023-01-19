"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ProductSetDistributionV2 import ProductSetDistributionV2





class ProductSetV2(BaseSchema):
    #  swagger.json

    
    size_distribution = fields.Nested(ProductSetDistributionV2, required=False)
    
    quantity = fields.Int(required=False)
    
