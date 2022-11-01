"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class CanBreakResponse(BaseSchema):
    #  swagger.json

    
    status = fields.Boolean(required=False)
    
    valid_actions = fields.Dict(required=False)
    
