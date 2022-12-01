"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class Identifiers(BaseSchema):
    #  swagger.json

    
    ean = fields.Str(required=False)
    
