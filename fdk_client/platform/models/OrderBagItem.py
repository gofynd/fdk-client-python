"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
















class OrderBagItem(BaseSchema):
    # Orders swagger.json

    
    l1_category = fields.List(fields.Str(required=False), required=False)
    
    l3_category = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
    image = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    brand = fields.Str(required=False)
    
    slug_key = fields.Str(required=False)
    

