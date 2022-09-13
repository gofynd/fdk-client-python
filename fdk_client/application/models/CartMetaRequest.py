"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .RevenueTaxDetail import RevenueTaxDetail










class CartMetaRequest(BaseSchema):
    # Cart swagger.json

    
    revenue_tax = fields.Nested(RevenueTaxDetail, required=False)
    
    checkout_mode = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    pick_up_customer_details = fields.Dict(required=False)
    
    comment = fields.Str(required=False)
    

