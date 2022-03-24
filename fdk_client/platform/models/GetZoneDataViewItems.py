"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema











from .GetZoneDataViewProduct import GetZoneDataViewProduct



from .GetZoneDataViewChannels import GetZoneDataViewChannels




class GetZoneDataViewItems(BaseSchema):
    # Serviceability swagger.json

    
    is_active = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    zone_id = fields.Str(required=False)
    
    pincodes_count = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    product = fields.Nested(GetZoneDataViewProduct, required=False)
    
    stores_count = fields.Int(required=False)
    
    channels = fields.Nested(GetZoneDataViewChannels, required=False)
    
    company_id = fields.Int(required=False)
    

