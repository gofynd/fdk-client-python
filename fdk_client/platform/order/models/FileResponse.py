"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












from .URL import URL









from .FileUploadResponse import FileUploadResponse





class FileResponse(BaseSchema):
    #  swagger.json

    
    content_type = fields.Str(required=False)
    
    operation = fields.Str(required=False)
    
    file_name = fields.Str(required=False)
    
    namespace = fields.Str(required=False)
    
    cdn = fields.Nested(URL, required=False)
    
    method = fields.Str(required=False)
    
    file_path = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    upload = fields.Nested(FileUploadResponse, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
