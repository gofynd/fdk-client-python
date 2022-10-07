"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class GenerateReportFilters(BaseSchema):
    # Finance swagger.json

    
    brand = fields.List(fields.Str(required=False), required=False)
    
    company = fields.List(fields.Str(required=False), required=False)
    
    channel = fields.List(fields.Str(required=False), required=False)
    

