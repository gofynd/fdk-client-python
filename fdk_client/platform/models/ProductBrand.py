"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Action import Action



from .Media1 import Media1


class ProductBrand(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    action = fields.Nested(Action, required=False)
    
    name = fields.Str(required=False)
    
    logo = fields.Nested(Media1, required=False)
    

