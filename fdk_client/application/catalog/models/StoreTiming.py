"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .Time import Time



from .Time import Time



class StoreTiming(BaseSchema):
    #  swagger.json

    
    open = fields.Boolean(required=False)
    
    weekday = fields.Str(required=False)
    
    opening = fields.Nested(Time, required=False)
    
    closing = fields.Nested(Time, required=False)
    
