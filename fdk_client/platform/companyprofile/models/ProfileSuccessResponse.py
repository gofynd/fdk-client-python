"""companyprofile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class ProfileSuccessResponse(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    
    uid = fields.Int(required=False)
    
