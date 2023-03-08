"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class GetZonesForZoneFromPincode(BaseSchema):
    # Serviceability swagger.json

    
    zone_id = fields.Str(required=False)
    
    assignment_preference = fields.Str(required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    type = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    

