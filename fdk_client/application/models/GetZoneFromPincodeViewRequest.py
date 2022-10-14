"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class GetZoneFromPincodeViewRequest(BaseSchema):
    # Logistic swagger.json

    
    pincode = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
