"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Action import Action







from .Media1 import Media1



class ProductBrand(BaseSchema):
    #  swagger.json

    
    action = fields.Nested(Action, required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    logo = fields.Nested(Media1, required=False)
    