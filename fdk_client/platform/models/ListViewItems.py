"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema













from .ListViewProduct import ListViewProduct

from .ListViewChannels import ListViewChannels




class ListViewItems(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    zone_id = fields.Str(required=False)
    
    stores_count = fields.Int(required=False)
    
    pincodes_count = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    product = fields.Nested(ListViewProduct, required=False)
    
    channels = fields.Nested(ListViewChannels, required=False)
    
    slug = fields.Str(required=False)
    

