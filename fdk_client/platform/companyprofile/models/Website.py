"""companyprofile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class Website(BaseSchema):
    #  swagger.json

    
    url = fields.Str(required=False)
    