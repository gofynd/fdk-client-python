"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class ManifestPage(BaseSchema):
    # Order swagger.json

    
    has_previous = fields.Boolean(required=False)
    
    current = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    has_next = fields.Boolean(required=False)
    
    size = fields.Str(required=False)
    
    total = fields.Int(required=False)
    

