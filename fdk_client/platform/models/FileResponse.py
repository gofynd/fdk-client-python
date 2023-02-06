"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .FileUploadResponse import FileUploadResponse













from .URL import URL


class FileResponse(BaseSchema):
    # Order swagger.json

    
    file_path = fields.Str(required=False)
    
    operation = fields.Str(required=False)
    
    upload = fields.Nested(FileUploadResponse, required=False)
    
    namespace = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    file_name = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    content_type = fields.Str(required=False)
    
    method = fields.Str(required=False)
    
    cdn = fields.Nested(URL, required=False)
    

