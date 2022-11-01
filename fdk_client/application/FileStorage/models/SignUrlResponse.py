"""FileStorage Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .Urls import Urls



class SignUrlResponse(BaseSchema):
    #  swagger.json

    
    urls = fields.List(fields.Nested(Urls, required=False), required=False)
    
