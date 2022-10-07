"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .GenerateReportMeta import GenerateReportMeta

from .GenerateReportFilters import GenerateReportFilters








class GenerateReportPlatform(BaseSchema):
    # Finance swagger.json

    
    meta = fields.Nested(GenerateReportMeta, required=False)
    
    filters = fields.Nested(GenerateReportFilters, required=False)
    
    report_id = fields.Str(required=False)
    
    end_date = fields.Str(required=False)
    
    start_date = fields.Str(required=False)
    

