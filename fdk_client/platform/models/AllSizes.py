"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .ValidateIdentifier import ValidateIdentifier












class AllSizes(BaseSchema):
    # Catalog swagger.json

    
    item_weight = fields.Float(required=False)
    
    size = fields.Raw(required=False)
    
    identifiers = fields.List(fields.Nested(ValidateIdentifier, required=False), required=False)
    
    item_weight_unit_of_measure = fields.Raw(required=False)
    
    item_width = fields.Float(required=False)
    
    item_height = fields.Float(required=False)
    
    item_dimensions_unit_of_measure = fields.Str(required=False)
    
    item_length = fields.Float(required=False)
    

