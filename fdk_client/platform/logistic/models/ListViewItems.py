"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .ListViewProduct import ListViewProduct









from .ListViewChannels import ListViewChannels







class ListViewItems(BaseSchema):
    #  swagger.json

    
    slug = fields.Str(required=False)
    
    pincodes_count = fields.Int(required=False)
    
    product = fields.Nested(ListViewProduct, required=False)
    
    stores_count = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    channels = fields.Nested(ListViewChannels, required=False)
    
    name = fields.Str(required=False)
    
    zone_id = fields.Str(required=False)
    
