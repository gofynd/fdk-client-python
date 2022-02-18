"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CreditSummary import CreditSummary




class CustomerCreditSummaryResponse(BaseSchema):
    # Payment swagger.json

    
    data = fields.List(fields.Nested(CreditSummary, required=False), required=False)
    
    success = fields.Boolean(required=False)
    

