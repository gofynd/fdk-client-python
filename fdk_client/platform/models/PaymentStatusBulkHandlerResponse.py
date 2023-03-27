"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .PaymentStatusObject import PaymentStatusObject






class PaymentStatusBulkHandlerResponse(BaseSchema):
    # Payment swagger.json

    
    success = fields.Str(required=False)
    
    count = fields.Int(required=False)
    
    data = fields.List(fields.Nested(PaymentStatusObject, required=False), required=False)
    
    status = fields.Int(required=False)
    
    error = fields.Str(required=False)
    

