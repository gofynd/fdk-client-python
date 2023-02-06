"""content Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














from .Action import Action



class SlideshowMedia(BaseSchema):
    #  swagger.json

    
    type = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    bg_color = fields.Str(required=False)
    
    duration = fields.Int(required=False)
    
    auto_decide_duration = fields.Boolean(required=False)
    
    action = fields.Nested(Action, required=False)
    
