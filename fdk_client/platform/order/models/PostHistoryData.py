"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class PostHistoryData(BaseSchema):
    #  swagger.json

    
    user_name = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
