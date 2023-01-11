"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .LocationTimingSerializer import LocationTimingSerializer



from .LocationTimingSerializer import LocationTimingSerializer







class LocationDayWiseSerializer(BaseSchema):
    #  swagger.json

    
    closing = fields.Nested(LocationTimingSerializer, required=False)
    
    opening = fields.Nested(LocationTimingSerializer, required=False)
    
    weekday = fields.Str(required=False)
    
    open = fields.Boolean(required=False)
    
