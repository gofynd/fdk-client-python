"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .EffectiveValues import EffectiveValues



from .MarkedValues import MarkedValues



class ItemPriceDetails(BaseSchema):
    #  swagger.json

    
    currency = fields.Str(required=False)
    
    effective = fields.Nested(EffectiveValues, required=False)
    
    marked = fields.Nested(MarkedValues, required=False)
    
