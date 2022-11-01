"""Configuration Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class Ios(BaseSchema):
    #  swagger.json

    
    application_id = fields.Str(required=False)
    
    api_key = fields.Str(required=False)
    
