"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class DisplayMeta1(BaseSchema):
    #  swagger.json

    
    description = fields.Str(required=False)
    
    offer_text = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
