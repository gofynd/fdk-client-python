"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class HolidayDateSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    end_date = fields.Str(required=False)
    
    start_date = fields.Str(required=False)
    

