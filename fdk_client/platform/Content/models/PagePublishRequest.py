"""Content Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class PagePublishRequest(BaseSchema):
    #  swagger.json

    
    publish = fields.Boolean(required=False)
    
