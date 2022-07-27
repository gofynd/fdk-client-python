"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class OrderErrorSchemaDataSet(BaseSchema):
    # Orders swagger.json

    
    reason = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
