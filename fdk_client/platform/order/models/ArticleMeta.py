"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class ArticleMeta(BaseSchema):
    #  swagger.json

    
    service = fields.Str(required=False)
    
