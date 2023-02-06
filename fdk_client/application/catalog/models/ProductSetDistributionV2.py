"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ProductSetDistributionSizeV2 import ProductSetDistributionSizeV2



class ProductSetDistributionV2(BaseSchema):
    #  swagger.json

    
    sizes = fields.List(fields.Nested(ProductSetDistributionSizeV2, required=False), required=False)
    
