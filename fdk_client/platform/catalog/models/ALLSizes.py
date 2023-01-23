"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
















from .ValidateIdentifier import ValidateIdentifier





class ALLSizes(BaseSchema):
    #  swagger.json

    
    item_length = fields.Float(required=False)
    
    size = fields.Raw(required=False)
    
    item_width = fields.Float(required=False)
    
    item_weight = fields.Float(required=False)
    
    item_height = fields.Float(required=False)
    
    item_dimensions_unit_of_measure = fields.Str(required=False)
    
    identifiers = fields.List(fields.Nested(ValidateIdentifier, required=False), required=False)
    
    item_weight_unit_of_measure = fields.Raw(required=False)
    
