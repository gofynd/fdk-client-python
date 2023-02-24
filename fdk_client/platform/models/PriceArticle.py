"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class PriceArticle(BaseSchema):
    # Catalog swagger.json

    
    currency = fields.Str(required=False)
    
    transfer = fields.Float(required=False)
    
    tp_notes = fields.Dict(required=False)
    
    effective = fields.Float(required=False)
    
    marked = fields.Float(required=False)
    

