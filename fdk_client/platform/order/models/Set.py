"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .SetSizeDistribution import SetSizeDistribution



class Set(BaseSchema):
    #  swagger.json

    
    quantity = fields.Int(required=False)
    
    size_distribution = fields.Nested(SetSizeDistribution, required=False)
    
