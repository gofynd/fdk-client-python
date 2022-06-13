"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class Document(BaseSchema):
    # Catalog swagger.json

    
    url = fields.Str(required=False)
    
    verified = fields.Boolean(required=False)
    
    value = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    legal_name = fields.Str(required=False)
    

