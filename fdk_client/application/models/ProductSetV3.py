"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ProductSetDistributionV3 import ProductSetDistributionV3


class ProductSetV3(BaseSchema):
    # Catalog swagger.json

    
    quantity = fields.Int(required=False)
    
    size_distribution = fields.Nested(ProductSetDistributionV3, required=False)
    

