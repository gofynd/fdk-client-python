"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class MarketPlacePdf(BaseSchema):
    #  swagger.json

    
    label = fields.Str(required=False)
    
    invoice = fields.Str(required=False)
    
