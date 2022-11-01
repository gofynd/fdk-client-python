"""User Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class FormRegisterRequestSchemaPhone(BaseSchema):
    #  swagger.json

    
    country_code = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
