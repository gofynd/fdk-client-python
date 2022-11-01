"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ActivityHistory import ActivityHistory



class GetActivityStatus(BaseSchema):
    #  swagger.json

    
    activity_history = fields.Nested(ActivityHistory, required=False)
    
