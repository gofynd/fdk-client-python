"""Payment Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class IntentAppErrorList(BaseSchema):
    #  swagger.json

    
    package_name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
