"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .PageResponseType import PageResponseType





class GetConfigResponse(BaseSchema):
    #  swagger.json

    
    page = fields.Nested(PageResponseType, required=False)
    
    data = fields.List(fields.Dict(required=False), required=False)
    
