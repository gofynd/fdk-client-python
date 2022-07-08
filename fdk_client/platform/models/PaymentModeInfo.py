"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class PaymentModeInfo(BaseSchema):
    # Orders swagger.json

    
    logo = fields.Str(required=False)
    
    type = fields.Str(required=False)
    

