"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class ShipmentTrackResponseBagListItemStatusesProgress(BaseSchema):
    #  swagger.json

    
    title = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    state = fields.Boolean(required=False)
    
