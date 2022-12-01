"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class ShipmentTrackResponseBagListItemDpDetails(BaseSchema):
    #  swagger.json

    
    tracking_no = fields.Str(required=False)
    
    courier = fields.Str(required=False)
    
