"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class BaseInfo(BaseSchema):
    #  swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
