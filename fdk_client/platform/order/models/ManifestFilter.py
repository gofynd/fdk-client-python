"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .DateRange import DateRange

















class ManifestFilter(BaseSchema):
    #  swagger.json

    
    date_range = fields.Nested(DateRange, required=False)
    
    sales_channel_name = fields.Str(required=False)
    
    dp_name = fields.Str(required=False)
    
    dp_ids = fields.Str(required=False)
    
    lane = fields.Str(required=False)
    
    sales_channels = fields.Str(required=False)
    
    stores = fields.Str(required=False)
    
    store_name = fields.Str(required=False)
    
