"""common Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class ApplicationCors(BaseSchema):
    #  swagger.json

    
    domains = fields.List(fields.Str(required=False), required=False)
    
