"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class PaymentModeInfo(BaseSchema):
    # Order swagger.json

    
    type = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    

