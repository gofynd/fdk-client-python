"""user Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class FlashCard(BaseSchema):
    #  swagger.json

    
    text = fields.Str(required=False)
    
    text_color = fields.Str(required=False)
    
    background_color = fields.Str(required=False)
    
