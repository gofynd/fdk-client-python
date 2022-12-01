"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class ZoneResponse(BaseSchema):
    #  swagger.json

    
    zone_id = fields.Str(required=False)
    
    status_code = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    
