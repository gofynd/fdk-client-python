"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class OrderBrandName(BaseSchema):
    # Order swagger.json

    
    id = fields.Int(required=False)
    
    logo = fields.Str(required=False)
    
    brand_name = fields.Str(required=False)
    
    created_on = fields.Int(required=False)
    
    company = fields.Str(required=False)
    
    modified_on = fields.Int(required=False)
    

