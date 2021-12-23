"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema



from .Media1 import Media1



from .Action import Action


class ProductBrand(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    logo = fields.Nested(Media1, required=False)
    
    name = fields.Str(required=False)
    
    action = fields.Nested(Action, required=False)
    

