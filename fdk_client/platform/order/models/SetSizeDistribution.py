"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Sizes import Sizes



class SetSizeDistribution(BaseSchema):
    #  swagger.json

    
    sizes = fields.Nested(Sizes, required=False)
    
