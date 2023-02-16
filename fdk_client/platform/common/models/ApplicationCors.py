"""common Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class ApplicationCors(BaseSchema):
    #  swagger.json

    
    domains = fields.List(fields.Str(required=False), required=False)
    
