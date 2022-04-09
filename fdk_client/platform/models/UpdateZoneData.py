"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ZoneProductTypes import ZoneProductTypes









from .GetZoneDataViewChannels import GetZoneDataViewChannels





from .ZoneMappingType import ZoneMappingType


class UpdateZoneData(BaseSchema):
    # Serviceability swagger.json

    
    is_active = fields.Boolean(required=False)
    
    product = fields.Nested(ZoneProductTypes, required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    company_id = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    region_type = fields.Str(required=False)
    
    channels = fields.List(fields.Nested(GetZoneDataViewChannels, required=False), required=False)
    
    zone_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    mapping = fields.List(fields.Nested(ZoneMappingType, required=False), required=False)
    

