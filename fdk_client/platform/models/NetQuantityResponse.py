"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class NetQuantityResponse(BaseSchema):
    # Catalog swagger.json

    
    unit = fields.Str(required=False)
    
    value = fields.Float(required=False)
    

