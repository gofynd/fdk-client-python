"""Inventory Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














from .ArchiveConfig import ArchiveConfig



class GoogleSpreadSheetConfig(BaseSchema):
    #  swagger.json

    
    range = fields.Str(required=False)
    
    sheet_id = fields.Str(required=False)
    
    client_secret_location = fields.Str(required=False)
    
    cred_storage_directory = fields.Str(required=False)
    
    local_dir = fields.Str(required=False)
    
    archive_config = fields.Nested(ArchiveConfig, required=False)
    
