"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class ProductSetDistributionSizeV2(BaseSchema):
    #  swagger.json

    
    size = fields.Str(required=False)
    
    pieces = fields.Int(required=False)
    
