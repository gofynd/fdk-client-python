"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class ArticleIdentifiers(BaseSchema):
    #  swagger.json

    
    ean = fields.Str(required=False)
    
