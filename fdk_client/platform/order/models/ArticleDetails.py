"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class ArticleDetails(BaseSchema):
    #  swagger.json

    
    status = fields.Dict(required=False)
    
