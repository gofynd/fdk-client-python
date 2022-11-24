"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class SuccessResponseGenerateBulk(BaseSchema):
    # DocumentEngine swagger.json

    
    success = fields.Boolean(required=False)
    

