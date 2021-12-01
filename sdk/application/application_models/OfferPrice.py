"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema












class OfferPrice(BaseSchema):

    
    effective = fields.Int(required=False)
    
    marked = fields.Int(required=False)
    
    bulk_effective = fields.Float(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    

