"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class TATTimestampResponse(BaseSchema):
    # Logistic swagger.json

    
    max = fields.Int(required=False)
    
    min = fields.Int(required=False)
    

