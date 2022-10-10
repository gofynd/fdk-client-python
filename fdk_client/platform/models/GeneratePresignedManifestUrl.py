"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class GeneratePresignedManifestUrl(BaseSchema):
    # DocumentEngine swagger.json

    
    manifest_id = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    

