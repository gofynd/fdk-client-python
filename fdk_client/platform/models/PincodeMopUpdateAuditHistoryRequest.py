"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class PincodeMopUpdateAuditHistoryRequest(BaseSchema):
    # Serviceability swagger.json

    
    entity_type = fields.Str(required=False)
    
    file_name = fields.Str(required=False)
    

