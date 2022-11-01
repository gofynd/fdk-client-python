"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .BuildVersion import BuildVersion





class BuildVersionHistory(BaseSchema):
    #  swagger.json

    
    versions = fields.Nested(BuildVersion, required=False)
    
    latest_available_version_name = fields.Str(required=False)
    
