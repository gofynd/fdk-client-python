"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .MarkedValues import MarkedValues

from .EffectiveValues import EffectiveValues


class ItemPriceDetails(BaseSchema):
    # Order swagger.json

    
    currency = fields.Str(required=False)
    
    marked = fields.Nested(MarkedValues, required=False)
    
    effective = fields.Nested(EffectiveValues, required=False)
    

