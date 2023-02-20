"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .PincodeMopUpdateAuditHistoryPaging import PincodeMopUpdateAuditHistoryPaging



from .PincodeMopUpdateAuditHistoryResponse import PincodeMopUpdateAuditHistoryResponse



class PincodeMopUpdateAuditHistoryResponseData(BaseSchema):
    #  swagger.json

    
    entity_type = fields.Str(required=False)
    
    page = fields.Nested(PincodeMopUpdateAuditHistoryPaging, required=False)
    
    data = fields.List(fields.Nested(PincodeMopUpdateAuditHistoryResponse, required=False), required=False)
    
