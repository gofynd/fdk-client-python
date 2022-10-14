"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class PaymentInfo(BaseSchema):
    # Order swagger.json

    
    logo = fields.Str(required=False)
    
    mop = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
