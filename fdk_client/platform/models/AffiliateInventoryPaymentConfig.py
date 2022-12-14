"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class AffiliateInventoryPaymentConfig(BaseSchema):
    # Order swagger.json

    
    source = fields.Str(required=False)
    
    mode_of_payment = fields.Str(required=False)
    
