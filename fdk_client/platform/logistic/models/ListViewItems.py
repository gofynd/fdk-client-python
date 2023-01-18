"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .ListViewProduct import ListViewProduct





from .ListViewChannels import ListViewChannels













class ListViewItems(BaseSchema):
    #  swagger.json

    
    zone_id = fields.Str(required=False)
    
    product = fields.Nested(ListViewProduct, required=False)
    
    is_active = fields.Boolean(required=False)
    
    channels = fields.Nested(ListViewChannels, required=False)
    
    pincodes_count = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    stores_count = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
