"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class CallbackUrl(BaseSchema):
    #  swagger.json

    
    app = fields.Str(required=False)
    
    web = fields.Str(required=False)
    
