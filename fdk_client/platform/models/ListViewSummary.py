"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class ListViewSummary(BaseSchema):
    # Serviceability swagger.json

    
    total_pincodes_served = fields.Int(required=False)
    
    total_active_zones = fields.Int(required=False)
    
    total_zones = fields.Int(required=False)
    

