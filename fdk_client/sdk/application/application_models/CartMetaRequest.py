"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema










class CartMetaRequest(BaseSchema):
    # Cart swagger.json

    
    checkout_mode = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    pick_up_customer_details = fields.Dict(required=False)
    

