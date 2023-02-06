"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class BulkActionResponse(BaseSchema):
    # Orders swagger.json

    
    message = fields.Str(required=False)
    
    status = fields.Boolean(required=False)
    

