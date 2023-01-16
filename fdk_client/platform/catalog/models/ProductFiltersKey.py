"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class ProductFiltersKey(BaseSchema):
    #  swagger.json

    
    logo = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    kind = fields.Str(required=False)
    
    operators = fields.List(fields.Str(required=False), required=False)
    
    display = fields.Str(required=False)
    