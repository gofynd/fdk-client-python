"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class GetZoneFromPincodeViewResponse(BaseSchema):
    # Logistic swagger.json

    
    serviceability_type = fields.Str(required=False)
    
    zones = fields.List(fields.Str(required=False), required=False)
    

