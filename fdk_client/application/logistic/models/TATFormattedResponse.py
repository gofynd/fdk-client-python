"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class TATFormattedResponse(BaseSchema):
    #  swagger.json

    
    min = fields.Str(required=False)
    
    max = fields.Str(required=False)
    