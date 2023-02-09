"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .PostActivityHistory import PostActivityHistory



class PostHistoryDict(BaseSchema):
    #  swagger.json

    
    activity_history = fields.Nested(PostActivityHistory, required=False)
    
