"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .TATTimestampResponse import TATTimestampResponse



from .TATFormattedResponse import TATFormattedResponse



class TATPromiseResponse(BaseSchema):
    #  swagger.json

    
    timestamp = fields.Nested(TATTimestampResponse, required=False)
    
    formatted = fields.Nested(TATFormattedResponse, required=False)
    
