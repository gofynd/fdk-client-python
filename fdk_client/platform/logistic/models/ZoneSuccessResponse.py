"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class ZoneSuccessResponse(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    
    status_code = fields.Int(required=False)
    
