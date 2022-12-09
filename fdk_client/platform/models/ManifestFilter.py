"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .DateRange import DateRange












class ManifestFilter(BaseSchema):
    # Orders swagger.json

    
    dp_name = fields.Str(required=False)
    
    sales_channels = fields.Str(required=False)
    
    date_range = fields.Nested(DateRange, required=False)
    
    store_name = fields.Str(required=False)
    
    sales_channel_name = fields.Str(required=False)
    
    dp_ids = fields.Str(required=False)
    
    lane = fields.Str(required=False)
    
    stores = fields.Str(required=False)
    

