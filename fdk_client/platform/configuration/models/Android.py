"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class Android(BaseSchema):
    #  swagger.json

    
    application_id = fields.Str(required=False)
    
    api_key = fields.Str(required=False)
    
