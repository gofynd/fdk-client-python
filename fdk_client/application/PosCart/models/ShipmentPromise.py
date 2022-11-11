"""PosCart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .PromiseTimestamp import PromiseTimestamp



from .PromiseFormatted import PromiseFormatted



class ShipmentPromise(BaseSchema):
    #  swagger.json

    
    timestamp = fields.Nested(PromiseTimestamp, required=False)
    
    formatted = fields.Nested(PromiseFormatted, required=False)
    
