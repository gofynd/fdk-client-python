"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ListViewChannels import ListViewChannels



from .ListViewProduct import ListViewProduct














class ListViewItems(BaseSchema):
    # Serviceability swagger.json

    
    channels = fields.Nested(ListViewChannels, required=False)
    
    is_active = fields.Boolean(required=False)
    
    product = fields.Nested(ListViewProduct, required=False)
    
    id = fields.Str(required=False)
    
    pincodes_count = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    stores_count = fields.Int(required=False)
    

