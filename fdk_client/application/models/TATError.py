"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class TATError(BaseSchema):
    # Logistic swagger.json

    
    value = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    type = fields.Str(required=False)
    

