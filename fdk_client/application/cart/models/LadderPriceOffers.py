"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .LadderPriceOffer import LadderPriceOffer



from .CurrencyInfo import CurrencyInfo



class LadderPriceOffers(BaseSchema):
    #  swagger.json

    
    available_offers = fields.List(fields.Nested(LadderPriceOffer, required=False), required=False)
    
    currency = fields.Nested(CurrencyInfo, required=False)
    
