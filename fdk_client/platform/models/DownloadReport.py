"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class DownloadReport(BaseSchema):
    # Finance swagger.json

    
    pagesize = fields.Int(required=False)
    
    end_date = fields.Str(required=False)
    
    page = fields.Int(required=False)
    
    start_date = fields.Str(required=False)
    

