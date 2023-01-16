"""poscart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .PromiseFormatted import PromiseFormatted



from .PromiseTimestamp import PromiseTimestamp



class ShipmentPromise(BaseSchema):
    #  swagger.json

    
    formatted = fields.Nested(PromiseFormatted, required=False)
    
    timestamp = fields.Nested(PromiseTimestamp, required=False)
    
