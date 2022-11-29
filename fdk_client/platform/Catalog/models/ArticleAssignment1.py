"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class ArticleAssignment1(BaseSchema):
    #  swagger.json

    
    strategy = fields.Str(required=False)
    
    level = fields.Str(required=False)
    
