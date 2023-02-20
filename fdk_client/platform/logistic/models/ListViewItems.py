"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .ListViewChannels import ListViewChannels



from .ListViewProduct import ListViewProduct













class ListViewItems(BaseSchema):
    #  swagger.json

    
    company_id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    channels = fields.Nested(ListViewChannels, required=False)
    
    product = fields.Nested(ListViewProduct, required=False)
    
    pincodes_count = fields.Int(required=False)
    
    stores_count = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    zone_id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
