"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class ProductFiltersKey(BaseSchema):
    #  swagger.json

    
    kind = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    operators = fields.List(fields.Str(required=False), required=False)
    
    logo = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
