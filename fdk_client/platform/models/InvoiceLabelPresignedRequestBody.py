"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class InvoiceLabelPresignedRequestBody(BaseSchema):
    # DocumentEngine swagger.json

    
    document_type = fields.Str(required=False)
    
    entity_id = fields.Str(required=False)
    
    expires_in = fields.Float(required=False)
    

