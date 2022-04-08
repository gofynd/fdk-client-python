"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class ZoneMappingType(BaseSchema):
    # Serviceability swagger.json

    
    country = fields.Str(required=False)
    
    state = fields.List(fields.Str(required=False), required=False)
    
    pincode = fields.List(fields.Str(required=False), required=False)
    

