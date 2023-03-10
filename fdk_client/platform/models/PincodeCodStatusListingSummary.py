"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class PincodeCodStatusListingSummary(BaseSchema):
    # Serviceability swagger.json

    
    total_active_pincodes = fields.Int(required=False)
    
    total_inactive_pincodes = fields.Int(required=False)
    

