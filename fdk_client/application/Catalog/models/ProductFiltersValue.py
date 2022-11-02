"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




























class ProductFiltersValue(BaseSchema):
    #  swagger.json

    
    is_selected = fields.Boolean(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    display_format = fields.Str(required=False)
    
    min = fields.Int(required=False)
    
    query_format = fields.Str(required=False)
    
    count = fields.Int(required=False)
    
    max = fields.Int(required=False)
    
    selected_min = fields.Int(required=False)
    
    selected_max = fields.Int(required=False)
    
    value = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    
