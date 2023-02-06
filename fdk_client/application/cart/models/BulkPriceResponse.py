"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .BulkPriceOffer import BulkPriceOffer



class BulkPriceResponse(BaseSchema):
    #  swagger.json

    
    data = fields.List(fields.Nested(BulkPriceOffer, required=False), required=False)
    
