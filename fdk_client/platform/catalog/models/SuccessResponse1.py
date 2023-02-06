"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class SuccessResponse1(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    
    uid = fields.Int(required=False)
    
