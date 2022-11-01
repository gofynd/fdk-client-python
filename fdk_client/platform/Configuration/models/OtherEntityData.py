"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class OtherEntityData(BaseSchema):
    #  swagger.json

    
    article_identifier = fields.Str(required=False)
    
