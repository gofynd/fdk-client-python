"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class GenerateReportMeta(BaseSchema):
    # Finance swagger.json

    
    brand = fields.Str(required=False)
    
    company = fields.Str(required=False)
    
    channel = fields.Str(required=False)
    

