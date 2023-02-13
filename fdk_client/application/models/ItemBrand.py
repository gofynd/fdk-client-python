"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class ItemBrand(BaseSchema):
    # Order swagger.json

    
    logo = fields.Str(required=False)
    
    name = fields.Str(required=False)
    

