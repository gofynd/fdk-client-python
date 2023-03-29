"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .EntitiesReasons import EntitiesReasons

from .ProductsReasons import ProductsReasons


class ReasonsData(BaseSchema):
    # Order swagger.json

    
    entities = fields.List(fields.Nested(EntitiesReasons, required=False), required=False)
    
    products = fields.List(fields.Nested(ProductsReasons, required=False), required=False)
    

