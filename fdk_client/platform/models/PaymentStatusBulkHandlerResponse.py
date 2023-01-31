"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PaymentStatusObject import PaymentStatusObject










class PaymentStatusBulkHandlerResponse(BaseSchema):
    # Payment swagger.json

    
    data = fields.List(fields.Nested(PaymentStatusObject, required=False), required=False)
    
    error = fields.Str(required=False)
    
    count = fields.Int(required=False)
    
    status = fields.Int(required=False)
    
    success = fields.Str(required=False)
    

