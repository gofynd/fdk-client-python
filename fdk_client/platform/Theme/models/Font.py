"""Theme Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .Variants import Variants



class Font(BaseSchema):
    #  swagger.json

    
    family = fields.Str(required=False)
    
    variants = fields.Nested(Variants, required=False)
    
