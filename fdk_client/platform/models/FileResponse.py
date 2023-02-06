"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .URL import URL















from .FileUploadResponse import FileUploadResponse




class FileResponse(BaseSchema):
    # Orders swagger.json

    
    cdn = fields.Nested(URL, required=False)
    
    operation = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    file_name = fields.Str(required=False)
    
    namespace = fields.Str(required=False)
    
    method = fields.Str(required=False)
    
    content_type = fields.Str(required=False)
    
    file_path = fields.Str(required=False)
    
    upload = fields.Nested(FileUploadResponse, required=False)
    
    size = fields.Int(required=False)
    

