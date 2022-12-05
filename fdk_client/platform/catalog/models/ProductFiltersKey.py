"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class ProductFiltersKey(BaseSchema):
    #  swagger.json

    
    operators = fields.List(fields.Str(required=False), required=False)
    
    kind = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
