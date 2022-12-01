"""inventory Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class ArchiveConfig(BaseSchema):
    #  swagger.json

    
    delete = fields.Boolean(required=False)
    
    archive = fields.Boolean(required=False)
    
    archive_dir = fields.Str(required=False)
    
