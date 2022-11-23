"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .TimeStampData import TimeStampData



class Promise1(BaseSchema):
    #  swagger.json

    
    show_promise = fields.Str(required=False)
    
    timestamp = fields.Nested(TimeStampData, required=False)
    
