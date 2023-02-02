"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .InventoryPayload import InventoryPayload







class InventoryRequestSchemaV2(BaseSchema):
    #  swagger.json

    
    payload = fields.List(fields.Nested(InventoryPayload, required=False), required=False)
    
    meta = fields.Dict(required=False)
    
    company_id = fields.Int(required=False)
    
