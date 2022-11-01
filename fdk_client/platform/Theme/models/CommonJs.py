"""Theme Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class CommonJs(BaseSchema):
    #  swagger.json

    
    link = fields.Str(required=False)
    
