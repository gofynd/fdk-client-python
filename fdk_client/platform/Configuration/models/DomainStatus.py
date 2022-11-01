"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class DomainStatus(BaseSchema):
    #  swagger.json

    
    display = fields.Str(required=False)
    
    status = fields.Boolean(required=False)
    
