"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
















class BuyerDetails(BaseSchema):
    # Order swagger.json

    
    city = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    address = fields.Str(required=False)
    
    ajio_site_id = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
