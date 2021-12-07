"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema










class ProductSize(BaseSchema):

    
    is_available = fields.Boolean(required=False)
    
    value = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    display = fields.Str(required=False)
    

