"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class DocumentsResponse(BaseSchema):
    # Serviceability swagger.json

    
    legal_name = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    verified = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    

