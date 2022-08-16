"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ZoneProductTypes import ZoneProductTypes

from .ZoneMappingType import ZoneMappingType









from .GetZoneDataViewChannels import GetZoneDataViewChannels










class GetZoneDataViewItems(BaseSchema):
    # Serviceability swagger.json

    
    slug = fields.Str(required=False)
    
    product = fields.Nested(ZoneProductTypes, required=False)
    
    mapping = fields.List(fields.Nested(ZoneMappingType, required=False), required=False)
    
    region_type = fields.Str(required=False)
    
    stores_count = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    channels = fields.List(fields.Nested(GetZoneDataViewChannels, required=False), required=False)
    
    pincodes_count = fields.Int(required=False)
    
    zone_id = fields.Str(required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    

