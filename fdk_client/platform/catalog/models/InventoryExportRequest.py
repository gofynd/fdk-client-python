"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .InventoryExportFilter import InventoryExportFilter









class InventoryExportRequest(BaseSchema):
    #  swagger.json

    
    filters = fields.Nested(InventoryExportFilter, required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    data = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
