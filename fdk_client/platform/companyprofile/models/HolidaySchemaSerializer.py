"""companyprofile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .HolidayDateSerializer import HolidayDateSerializer





class HolidaySchemaSerializer(BaseSchema):
    #  swagger.json

    
    title = fields.Str(required=False)
    
    date = fields.Nested(HolidayDateSerializer, required=False)
    
    holiday_type = fields.Str(required=False)
    