"""Configuration Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class OS(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    version = fields.Str(required=False)
    
