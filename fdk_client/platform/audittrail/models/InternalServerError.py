"""audittrail Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class InternalServerError(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
