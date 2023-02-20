"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class PincodeMopUpdateAuditHistoryRequest(BaseSchema):
    #  swagger.json

    
    entity_type = fields.Str(required=False)
    
    file_name = fields.Str(required=False)
    
