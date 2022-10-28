"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .ListViewChannels import ListViewChannels







from .ListViewProduct import ListViewProduct




class ListViewItems(BaseSchema):
    # Serviceability swagger.json

    
    is_active = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    stores_count = fields.Int(required=False)
    
    channels = fields.Nested(ListViewChannels, required=False)
    
    company_id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    pincodes_count = fields.Int(required=False)
    
    product = fields.Nested(ListViewProduct, required=False)
    
    zone_id = fields.Str(required=False)
    

