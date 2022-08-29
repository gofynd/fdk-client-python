"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class OrderErrorSchemaDataSet(BaseSchema):
    # Orders swagger.json

    
    success = fields.Boolean(required=False)
    
    reason = fields.Str(required=False)
    

