"""content Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class Language(BaseSchema):
    #  swagger.json

    
    display = fields.Str(required=False)
    