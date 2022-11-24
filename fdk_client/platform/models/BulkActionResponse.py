"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class BulkActionResponse(BaseSchema):
    # Orders swagger.json

    
    status = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    

