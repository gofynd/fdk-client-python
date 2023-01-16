"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class CustomerDetailsResponse(BaseSchema):
    # Order swagger.json

    
    shipment_id = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    

