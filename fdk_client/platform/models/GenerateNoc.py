"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema











from .SellerAddress import SellerAddress

from .SellerAddress import SellerAddress


class GenerateNoc(BaseSchema):
    # DocumentEngine swagger.json

    
    uid = fields.Str(required=False)
    
    seller_name = fields.Str(required=False)
    
    seller_gstin = fields.Str(required=False)
    
    fc_gstin = fields.Str(required=False)
    
    template_id = fields.Float(required=False)
    
    fc_address = fields.Nested(SellerAddress, required=False)
    
    seller_address = fields.Nested(SellerAddress, required=False)
    

