"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .InventoryFailedReason import InventoryFailedReason



from .InventoryPayload import InventoryPayload



class InventoryResponseItem(BaseSchema):
    #  swagger.json

    
    reason = fields.Nested(InventoryFailedReason, required=False)
    
    data = fields.Nested(InventoryPayload, required=False)
    
