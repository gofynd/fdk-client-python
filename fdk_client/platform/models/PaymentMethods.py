"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class PaymentMethods(BaseSchema):
    # Order swagger.json

    
    mode = fields.Str(required=False)
    
    collect_by = fields.Str(required=False)
    
    refund_by = fields.Str(required=False)
    

