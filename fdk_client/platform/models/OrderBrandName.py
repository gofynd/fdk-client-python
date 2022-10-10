"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class OrderBrandName(BaseSchema):
    # Orders swagger.json

    
    company = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    brand_name = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    modified_on = fields.Int(required=False)
    
    created_on = fields.Int(required=False)
    
