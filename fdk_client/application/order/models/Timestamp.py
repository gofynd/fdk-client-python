"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class Timestamp(BaseSchema):
    #  swagger.json

    
    show_promise = fields.Boolean(required=False)
    
    min = fields.Str(required=False)
    
    max = fields.Str(required=False)
    
