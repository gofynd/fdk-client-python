"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class ManifestPage(BaseSchema):
    # Order swagger.json

    
    total = fields.Int(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    size = fields.Str(required=False)
    
    current = fields.Str(required=False)
    
    has_next = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    

