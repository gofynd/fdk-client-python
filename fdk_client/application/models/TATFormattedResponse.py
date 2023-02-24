"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class TATFormattedResponse(BaseSchema):
    # Logistic swagger.json

    
    max = fields.Str(required=False)
    
    min = fields.Str(required=False)
    

