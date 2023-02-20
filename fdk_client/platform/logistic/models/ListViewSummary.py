"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class ListViewSummary(BaseSchema):
    #  swagger.json

    
    total_active_zones = fields.Int(required=False)
    
    total_pincodes_served = fields.Int(required=False)
    
    total_zones = fields.Int(required=False)
    
