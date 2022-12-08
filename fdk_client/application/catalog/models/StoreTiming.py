"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .Time import Time



from .Time import Time





class StoreTiming(BaseSchema):
    #  swagger.json

    
    weekday = fields.Str(required=False)
    
    closing = fields.Nested(Time, required=False)
    
    opening = fields.Nested(Time, required=False)
    
    open = fields.Boolean(required=False)
    
