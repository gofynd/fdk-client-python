"""Theme Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .Variants import Variants



class Font(BaseSchema):
    #  swagger.json

    
    family = fields.Str(required=False)
    
    variants = fields.Nested(Variants, required=False)
    
