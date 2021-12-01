"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema










class Price(BaseSchema):

    
    currency_code = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    min = fields.Float(required=False)
    
    max = fields.Float(required=False)
    

