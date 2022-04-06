"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .GetZoneDataViewChannels import GetZoneDataViewChannels

from .ZoneProductTypes import ZoneProductTypes













from .ZoneMappingType import ZoneMappingType




class GetZoneDataViewItems(BaseSchema):
    # Serviceability swagger.json

    
    pincodes_count = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    channels = fields.List(fields.Nested(GetZoneDataViewChannels, required=False), required=False)
    
    product = fields.Nested(ZoneProductTypes, required=False)
    
    name = fields.Str(required=False)
    
    region_type = fields.Str(required=False)
    
    stores_count = fields.Int(required=False)
    
    zone_id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    mapping = fields.List(fields.Nested(ZoneMappingType, required=False), required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    

