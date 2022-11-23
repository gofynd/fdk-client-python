"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .ProductSetDistributionV2 import ProductSetDistributionV2



class ProductSetV2(BaseSchema):
    #  swagger.json

    
    quantity = fields.Int(required=False)
    
    size_distribution = fields.Nested(ProductSetDistributionV2, required=False)
    
