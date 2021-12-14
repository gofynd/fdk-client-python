"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema








class CurrencyFeature(BaseSchema):
    # Configuration swagger.json

    
    value = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    default_currency = fields.Str(required=False)
    

