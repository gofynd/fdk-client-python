"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class ZoneResponse(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Boolean(required=False)
    
    zone_id = fields.Str(required=False)
    
    status_code = fields.Int(required=False)
    

