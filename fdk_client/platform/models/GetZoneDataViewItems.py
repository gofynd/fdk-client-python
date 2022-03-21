"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .GetZoneDataViewChannels import GetZoneDataViewChannels



from .GetZoneDataViewProduct import GetZoneDataViewProduct














class GetZoneDataViewItems(BaseSchema):
    # Serviceability swagger.json

    
    channels = fields.Nested(GetZoneDataViewChannels, required=False)
    
    is_active = fields.Boolean(required=False)
    
    product = fields.Nested(GetZoneDataViewProduct, required=False)
    
    pincodes_count = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    stores_count = fields.Int(required=False)
    
    zone_id = fields.Str(required=False)
    

