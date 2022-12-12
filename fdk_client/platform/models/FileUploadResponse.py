"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class FileUploadResponse(BaseSchema):
    # Order swagger.json

    
    expiry = fields.Int(required=False)
    
    url = fields.Str(required=False)
    

