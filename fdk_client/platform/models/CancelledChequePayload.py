"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class CancelledChequePayload(BaseSchema):
    # Payment swagger.json

    
    document_mandatory = fields.Boolean(required=False)
    
    enabled = fields.Boolean(required=False)
    

