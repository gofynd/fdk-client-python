"""FileStorage Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Urls import Urls



class SignUrlResponse(BaseSchema):
    #  swagger.json

    
    urls = fields.List(fields.Nested(Urls, required=False), required=False)
    
