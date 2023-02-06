"""user Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class LookAndFeel(BaseSchema):
    #  swagger.json

    
    card_position = fields.Str(required=False)
    
    background_color = fields.Str(required=False)
    
