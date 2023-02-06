"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .LogisticTimestamp import LogisticTimestamp



from .Formatted import Formatted



class LogisticPromise(BaseSchema):
    #  swagger.json

    
    timestamp = fields.Nested(LogisticTimestamp, required=False)
    
    formatted = fields.Nested(Formatted, required=False)
    
