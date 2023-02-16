"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class MarketPlacePdf(BaseSchema):
    #  swagger.json

    
    invoice = fields.Str(required=False)
    
    label = fields.Str(required=False)
    
