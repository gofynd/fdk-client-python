"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class FileUploadResponse(BaseSchema):
    # Order swagger.json

    
    url = fields.Str(required=False)
    
    expiry = fields.Int(required=False)
    

