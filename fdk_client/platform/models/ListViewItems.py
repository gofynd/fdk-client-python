"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ListViewProduct import ListViewProduct





from .ListViewChannels import ListViewChannels










class ListViewItems(BaseSchema):
    # Serviceability swagger.json

    
    slug = fields.Str(required=False)
    
    product = fields.Nested(ListViewProduct, required=False)
    
    company_id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    channels = fields.Nested(ListViewChannels, required=False)
    
    pincodes_count = fields.Int(required=False)
    
    stores_count = fields.Int(required=False)
    
    zone_id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    

