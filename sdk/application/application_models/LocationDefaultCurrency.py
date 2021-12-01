"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema








class LocationDefaultCurrency(BaseSchema):

    
    name = fields.Str(required=False)
    
    symbol = fields.Str(required=False)
    
    code = fields.Str(required=False)
    

