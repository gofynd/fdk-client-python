"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class PincodeMopData(BaseSchema):
    # Serviceability swagger.json

    
    pincodes = fields.List(fields.Int(required=False), required=False)
    
    country = fields.Str(required=False)
    
    action = fields.Str(required=False)
    

