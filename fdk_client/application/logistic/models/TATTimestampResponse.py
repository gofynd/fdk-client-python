"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class TATTimestampResponse(BaseSchema):
    #  swagger.json

    
    max = fields.Int(required=False)
    
    min = fields.Int(required=False)
    
