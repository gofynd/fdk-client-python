"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .ZoneMappingType import ZoneMappingType

from .GetZoneDataViewChannels import GetZoneDataViewChannels









from .ZoneProductTypes import ZoneProductTypes








class GetZoneDataViewItems(BaseSchema):
    # Serviceability swagger.json

    
    zone_id = fields.Str(required=False)
    
    stores_count = fields.Int(required=False)
    
    mapping = fields.List(fields.Nested(ZoneMappingType, required=False), required=False)
    
    channels = fields.List(fields.Nested(GetZoneDataViewChannels, required=False), required=False)
    
    region_type = fields.Str(required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    pincodes_count = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    product = fields.Nested(ZoneProductTypes, required=False)
    
    company_id = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    

