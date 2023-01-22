"""poscart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .PickupStoreDetail import PickupStoreDetail



class StoreDetailsResponse(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(PickupStoreDetail, required=False), required=False)
    