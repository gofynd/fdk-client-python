"""billing Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class Phone(BaseSchema):
    #  swagger.json

    
    phone_number = fields.Str(required=False)
    
    phone_country_code = fields.Str(required=False)
    
