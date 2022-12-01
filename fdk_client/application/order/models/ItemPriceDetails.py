"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .MarkedValues import MarkedValues



from .EffectiveValues import EffectiveValues





class ItemPriceDetails(BaseSchema):
    #  swagger.json

    
    marked = fields.Nested(MarkedValues, required=False)
    
    effective = fields.Nested(EffectiveValues, required=False)
    
    currency = fields.Str(required=False)
    
