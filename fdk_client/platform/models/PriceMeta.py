"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class PriceMeta(BaseSchema):
    # Catalog swagger.json

    
    tp_notes = fields.Dict(required=False)
    
    transfer = fields.Float(required=False)
    
    marked = fields.Float(required=False)
    
    effective = fields.Float(required=False)
    
    currency = fields.Str(required=False)
    

