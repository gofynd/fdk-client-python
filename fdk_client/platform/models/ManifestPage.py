"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class ManifestPage(BaseSchema):
    # Orders swagger.json

    
    current = fields.Str(required=False)
    
    has_next = fields.Boolean(required=False)
    
    size = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    total = fields.Int(required=False)
    
    has_previous = fields.Boolean(required=False)
    

