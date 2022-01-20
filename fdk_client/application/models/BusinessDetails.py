"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .Address import Address
















class BusinessDetails(BaseSchema):
    # Payment swagger.json

    
    fssai = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    shop_and_establishment = fields.Dict(required=False)
    
    address = fields.List(fields.Nested(Address, required=False), required=False)
    
    pan = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    business_type = fields.Str(required=False)
    
    vintage = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    business_ownership_type = fields.Str(required=False)
    
    fda = fields.Str(required=False)
    
