"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .TimeStampData import TimeStampData





class Promise(BaseSchema):
    #  swagger.json

    
    timestamp = fields.Nested(TimeStampData, required=False)
    
    show_promise = fields.Boolean(required=False)
    
