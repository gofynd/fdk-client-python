"""Content Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class DataLoaderResetResponseSchema(BaseSchema):
    #  swagger.json

    
    reset = fields.Str(required=False)
    
