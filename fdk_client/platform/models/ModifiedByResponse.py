"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class ModifiedByResponse(BaseSchema):
    # Serviceability swagger.json

    
    username = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    

