"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .HolidayDateSerializer import HolidayDateSerializer


class HolidaySchemaSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    holiday_type = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    date = fields.Nested(HolidayDateSerializer, required=False)
    

