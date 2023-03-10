"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .PincodeMopUpdateAuditHistoryPaging import PincodeMopUpdateAuditHistoryPaging

from .PincodeMopUpdateAuditHistoryResponse import PincodeMopUpdateAuditHistoryResponse


class PincodeMopUpdateAuditHistoryResponseData(BaseSchema):
    # Serviceability swagger.json

    
    entity_type = fields.Str(required=False)
    
    page = fields.Nested(PincodeMopUpdateAuditHistoryPaging, required=False)
    
    data = fields.List(fields.Nested(PincodeMopUpdateAuditHistoryResponse, required=False), required=False)
    

