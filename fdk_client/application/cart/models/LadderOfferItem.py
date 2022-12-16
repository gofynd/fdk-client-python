"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .LadderPrice import LadderPrice









class LadderOfferItem(BaseSchema):
    #  swagger.json

    
    margin = fields.Int(required=False)
    
    price = fields.Nested(LadderPrice, required=False)
    
    min_quantity = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    max_quantity = fields.Int(required=False)
    