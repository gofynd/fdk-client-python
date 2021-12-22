"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .LocationTimingSerializer import LocationTimingSerializer



from .LocationTimingSerializer import LocationTimingSerializer




class LocationDayWiseSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    opening = fields.Nested(LocationTimingSerializer, required=False)
    
    open = fields.Boolean(required=False)
    
    closing = fields.Nested(LocationTimingSerializer, required=False)
    
    weekday = fields.Str(required=False)
    

