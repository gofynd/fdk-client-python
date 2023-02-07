"""poscart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class OfferSeller(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
