"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class CardPaymentGateway(BaseSchema):
    # Payment swagger.json

    
    api = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    customer_id = fields.Str(required=False)
    

