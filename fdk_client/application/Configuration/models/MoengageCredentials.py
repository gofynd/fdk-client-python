"""Configuration Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class MoengageCredentials(BaseSchema):
    #  swagger.json

    
    app_id = fields.Str(required=False)
    
