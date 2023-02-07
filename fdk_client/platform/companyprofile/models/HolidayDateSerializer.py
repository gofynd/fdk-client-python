"""companyprofile Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class HolidayDateSerializer(BaseSchema):
    #  swagger.json

    
    end_date = fields.Str(required=False)
    
    start_date = fields.Str(required=False)
    
