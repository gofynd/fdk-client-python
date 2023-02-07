"""theme Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class Sections(BaseSchema):
    #  swagger.json

    
    attributes = fields.Str(required=False)
    
