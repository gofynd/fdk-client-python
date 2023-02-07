"""inventory Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema


















from .ArchiveConfig import ArchiveConfig



class HttpConfig(BaseSchema):
    #  swagger.json

    
    hosturl = fields.Str(required=False)
    
    username = fields.Str(required=False)
    
    password = fields.Str(required=False)
    
    request_params = fields.Dict(required=False)
    
    http_method = fields.Str(required=False)
    
    request_payload = fields.Str(required=False)
    
    local_path = fields.Str(required=False)
    
    archive_config = fields.Nested(ArchiveConfig, required=False)
    
