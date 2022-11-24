"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class EffectiveValues(BaseSchema):
    # Order swagger.json

    
    min = fields.Float(required=False)
    
    max = fields.Float(required=False)
    

