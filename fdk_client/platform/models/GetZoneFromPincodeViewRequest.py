"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class GetZoneFromPincodeViewRequest(BaseSchema):
    # Serviceability swagger.json

    
    country = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    

