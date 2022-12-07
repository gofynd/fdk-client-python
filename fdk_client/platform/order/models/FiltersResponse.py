"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class FiltersResponse(BaseSchema):
    #  swagger.json

    
    advance = fields.List(fields.Dict(required=False), required=False)
    
