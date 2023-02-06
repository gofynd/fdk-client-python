"""content Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class PageSpec(BaseSchema):
    #  swagger.json

    
    specifications = fields.List(fields.Dict(required=False), required=False)
    
