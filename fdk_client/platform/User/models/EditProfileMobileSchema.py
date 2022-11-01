"""User Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class EditProfileMobileSchema(BaseSchema):
    #  swagger.json

    
    phone = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
