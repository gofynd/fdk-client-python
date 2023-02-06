"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .GetZonesForZoneFromPincode import GetZonesForZoneFromPincode




class GetZoneFromPincodeViewResponse(BaseSchema):
    # Serviceability swagger.json

    
    zones = fields.List(fields.Nested(GetZonesForZoneFromPincode, required=False), required=False)
    
    serviceability_type = fields.Str(required=False)
    

