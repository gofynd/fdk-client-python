"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class ResponseDetail(BaseSchema):
    # Order swagger.json

    
    message = fields.List(fields.Str(required=False), required=False)
    
    success = fields.Boolean(required=False)
    

