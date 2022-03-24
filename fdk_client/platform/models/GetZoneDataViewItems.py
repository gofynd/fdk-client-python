"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .GetZoneDataViewProduct import GetZoneDataViewProduct













from .GetZoneDataViewChannels import GetZoneDataViewChannels




class GetZoneDataViewItems(BaseSchema):
    # Serviceability swagger.json

    
    product = fields.Nested(GetZoneDataViewProduct, required=False)
    
    is_active = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    stores_count = fields.Int(required=False)
    
    zone_id = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    channels = fields.Nested(GetZoneDataViewChannels, required=False)
    
    pincodes_count = fields.Int(required=False)
    

