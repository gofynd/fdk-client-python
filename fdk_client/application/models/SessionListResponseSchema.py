"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class SessionListResponseSchema(BaseSchema):
    # User swagger.json

    
    items = fields.List(fields.Str(required=False), required=False)
    

