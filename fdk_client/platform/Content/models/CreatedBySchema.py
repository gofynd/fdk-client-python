"""Content Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class CreatedBySchema(BaseSchema):
    #  swagger.json

    
    id = fields.Str(required=False)
    
