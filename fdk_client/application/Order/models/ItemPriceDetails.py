"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .MarkedValues import MarkedValues



from .EffectiveValues import EffectiveValues



class ItemPriceDetails(BaseSchema):
    #  swagger.json

    
    currency = fields.Str(required=False)
    
    marked = fields.Nested(MarkedValues, required=False)
    
    effective = fields.Nested(EffectiveValues, required=False)
    
