"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Page import Page












class GenerateReportJson(BaseSchema):
    # Finance swagger.json

    
    page = fields.Nested(Page, required=False)
    
    item_count = fields.Int(required=False)
    
    items = fields.List(fields.List(fields.Str(required=False), required=False), required=False)
    
    headers = fields.List(fields.Str(required=False), required=False)
    
    end_date = fields.Str(required=False)
    
    start_date = fields.Str(required=False)
    

