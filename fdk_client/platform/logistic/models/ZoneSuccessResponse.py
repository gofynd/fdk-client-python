"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class ZoneSuccessResponse(BaseSchema):
    #  swagger.json

    
    status_code = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    
