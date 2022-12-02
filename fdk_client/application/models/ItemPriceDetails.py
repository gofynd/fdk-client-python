"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .EffectiveValues import EffectiveValues

from .MarkedValues import MarkedValues




class ItemPriceDetails(BaseSchema):
    # Order swagger.json

    
    effective = fields.Nested(EffectiveValues, required=False)
    
    marked = fields.Nested(MarkedValues, required=False)
    
    currency = fields.Str(required=False)
    

