"""user Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class EditMobileRequestSchema(BaseSchema):
    #  swagger.json

    
    country_code = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
