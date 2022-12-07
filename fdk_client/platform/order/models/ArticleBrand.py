"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class ArticleBrand(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    id = fields.Int(required=False)
    