"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .InventoryPayload import InventoryPayload



from .InventoryFailedReason import InventoryFailedReason



class InventoryResponseItem(BaseSchema):
    #  swagger.json

    
    data = fields.Nested(InventoryPayload, required=False)
    
    reason = fields.Nested(InventoryFailedReason, required=False)
    
