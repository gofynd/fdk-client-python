"""User Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class ArchiveUserSuccess(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    
