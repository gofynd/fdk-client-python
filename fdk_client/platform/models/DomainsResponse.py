"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Domain import Domain












class DomainsResponse(BaseSchema):
    # Configuration swagger.json

    
    domains = fields.List(fields.Nested(Domain, required=False), required=False)
    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    verified = fields.Boolean(required=False)
    
    is_primary = fields.Boolean(required=False)
    
    is_shortlink = fields.Boolean(required=False)
    

