"""partner Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class RemoveProxyResponse(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    
