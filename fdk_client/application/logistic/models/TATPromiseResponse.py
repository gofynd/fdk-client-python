"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .TATFormattedResponse import TATFormattedResponse



from .TATTimestampResponse import TATTimestampResponse



class TATPromiseResponse(BaseSchema):
    #  swagger.json

    
    formatted = fields.Nested(TATFormattedResponse, required=False)
    
    timestamp = fields.Nested(TATTimestampResponse, required=False)
    
