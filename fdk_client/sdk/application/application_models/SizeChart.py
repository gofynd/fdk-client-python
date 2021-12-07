"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .ColumnHeaders import ColumnHeaders







from .SizeChartValues import SizeChartValues






class SizeChart(BaseSchema):

    
    headers = fields.Nested(ColumnHeaders, required=False)
    
    description = fields.Str(required=False)
    
    size_tip = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    sizes = fields.List(fields.Nested(SizeChartValues, required=False), required=False)
    
    image = fields.Str(required=False)
    
    unit = fields.Str(required=False)
    

