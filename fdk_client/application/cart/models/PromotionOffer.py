"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














class PromotionOffer(BaseSchema):
    #  swagger.json

    
    id = fields.Str(required=False)
    
    valid_till = fields.Str(required=False)
    
    offer_text = fields.Str(required=False)
    
    promotion_group = fields.Str(required=False)
    
    description = fields.Str(required=False)
    