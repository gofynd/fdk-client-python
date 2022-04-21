"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema











from .ZoneMappingType import ZoneMappingType

from .ZoneProductTypes import ZoneProductTypes

from .GetZoneDataViewChannels import GetZoneDataViewChannels




class CreateZoneData(BaseSchema):
    # Serviceability swagger.json

    
    region_type = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    mapping = fields.List(fields.Nested(ZoneMappingType, required=False), required=False)
    
    product = fields.Nested(ZoneProductTypes, required=False)
    
    channels = fields.List(fields.Nested(GetZoneDataViewChannels, required=False), required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    

