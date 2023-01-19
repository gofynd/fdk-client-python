"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ActionInfo import ActionInfo



class GetActionsResponse(BaseSchema):
    #  swagger.json

    
    permissions = fields.Nested(ActionInfo, required=False)
    
