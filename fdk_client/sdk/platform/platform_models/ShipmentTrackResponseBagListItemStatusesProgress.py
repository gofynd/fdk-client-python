"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class ShipmentTrackResponseBagListItemStatusesProgress(BaseSchema):
    # Order swagger.json

    
    title = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    state = fields.Boolean(required=False)
    

