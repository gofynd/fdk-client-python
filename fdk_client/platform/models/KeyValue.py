"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class KeyValue(BaseSchema):
    # Lead swagger.json

    
    key = fields.Str(required=False)
    
    value = fields.Str(required=False)
    

