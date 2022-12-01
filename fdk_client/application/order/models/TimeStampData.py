"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class TimeStampData(BaseSchema):
    #  swagger.json

    
    max = fields.Str(required=False)
    
    min = fields.Str(required=False)
    
