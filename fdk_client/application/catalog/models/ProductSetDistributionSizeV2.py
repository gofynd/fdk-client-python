"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class ProductSetDistributionSizeV2(BaseSchema):
    #  swagger.json

    
    pieces = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
