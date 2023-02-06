"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class Identifiers(BaseSchema):
    # Order swagger.json

    
    sku_code = fields.Str(required=False)
    
    ean = fields.Str(required=False)
    

