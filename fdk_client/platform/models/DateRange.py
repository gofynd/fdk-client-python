"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class DateRange(BaseSchema):
    # Order swagger.json

    
    to_date = fields.Str(required=False)
    
    from_date = fields.Str(required=False)
    
